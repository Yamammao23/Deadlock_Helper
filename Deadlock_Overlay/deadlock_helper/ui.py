import tkinter as tk
from .screen import get_secondary_monitor
from .region_selector import select_region
from .config import load_region, save_region

def start_main_app():
    monitor = get_secondary_monitor()
    selected_region = load_region()

    def on_select_region():
        nonlocal selected_region
        selected_region = select_region()
        if selected_region:
            update_region_display(selected_region)
            save_region(selected_region)

    def update_region_display(region):
        if region:
            region_status.set("Region selected ✅")
            preview_button.config(state="normal")
        else:
            region_status.set("No region selected ❌")
            preview_button.config(state="disabled")

    def show_region_preview():
        if not selected_region:
            return

        preview = tk.Toplevel()
        preview.attributes("-topmost", True)
        preview.attributes("-alpha", 0.3)
        preview.overrideredirect(True)
        preview.geometry(f"{selected_region['width']}x{selected_region['height']}+{selected_region['left']}+{selected_region['top']}")
        preview.configure(bg='red')
        preview.after(1500, preview.destroy)

    # ---- UI Setup ----
    root = tk.Tk()
    root.title("Deadlock Helper")

    width, height = 400, 600
    x, y = monitor.x + 100, monitor.y + 100
    root.geometry(f"{width}x{height}+{x}+{y}")

    tk.Label(root, text="Deadlock Helper", font=("Helvetica", 20)).pack(pady=10)
    tk.Button(root, text="Select Region", command=on_select_region).pack(pady=10)

    region_status = tk.StringVar()
    region_label = tk.Label(root, textvariable=region_status)
    region_label.pack(pady=5)

    preview_button = tk.Button(root, text="Preview Region", command=show_region_preview, state="disabled")
    preview_button.pack(pady=5)

    tk.Button(root, text="Exit", command=root.destroy).pack(pady=20)

    update_region_display(selected_region)

    root.mainloop()