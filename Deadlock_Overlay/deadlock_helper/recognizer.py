import os
import cv2
import numpy as np
import mss
from PIL import Image

# Folder containing reference images of character portraits
CHARACTER_DIR = "deadlock_helper/data/portraits"
MATCH_THRESHOLD = 0.85

def capture_top_bar(region=None):
    """
    Capture a region of the screen. If no region is provided, capture the top part.
    Region is a dict: {'top': int, 'left': int, 'width': int, 'height': int}
    """
    with mss.mss() as sct:
        if region is None:
            monitor = sct.monitors[1]  # Primary monitor (index may vary)
            region = {
                "top": monitor["top"],
                "left": monitor["left"],
                "width": monitor["width"],
                "height": 120,  # Adjust based on top bar size
            }

        screenshot = sct.grab(region)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return np.array(img)


def detect_characters(screenshot_image):
    """
    Run template matching to find known characters in the screenshot.
    Returns a list of matched character names.
    """
    found = []

    for filename in os.listdir(CHARACTER_DIR):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        character_name = os.path.splitext(filename)[0]
        template = cv2.imread(os.path.join(CHARACTER_DIR, filename))
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        screenshot_gray = cv2.cvtColor(screenshot_image, cv2.COLOR_RGB2GRAY)

        result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= MATCH_THRESHOLD:
            found.append(character_name)

    return found
