import json
import os

CONFIG_FILE = "deadlock_helper/config.json"

def load_region():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                if all(k in data for k in ("left", "top", "width", "height")):
                    return data
        except Exception as e:
            print(f"Error loading region config: {e}")
    return None

def save_region(region):
    try:
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            json.dump(region, f, indent=4)
    except Exception as e:
        print(f"Error saving region config: {e}")