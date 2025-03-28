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
        if not region:
            print("[DEBUG] Empty region, removing config file.")
            if os.path.exists(CONFIG_FILE):
                os.remove(CONFIG_FILE)
            return

        print("[DEBUG] Saving region to:", CONFIG_FILE)
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)

        with open(CONFIG_FILE, "w") as f:
            json.dump(region, f, indent=4)

        print("[DEBUG] Region successfully written to config.json")
    except Exception as e:
        print("[ERROR] Failed to save region:", e)

    