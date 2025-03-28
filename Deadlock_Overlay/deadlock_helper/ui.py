import tkinter as tk
from .screen import get_secondary_monitor
from .region_selector import select_region
from .config import load_region, save_region

def start_main_app():
    monitor = get_secondary_monitor()
    selected_region = load_region()

    font_main = ("Segoe UI", 14)
    font_title = ("Segoe UI", 18, "bold")

    # Functions

    # Select a region
    def on_select_region():
        nonlocal selected_region
        try:
            print("[DEBUG] Select Region button clicked")
            region = select_region()
            print("[DEBUG] Region selected returned:", region)

            # Validate the region
            if region and all(k in region for k in ("left", "top", "width", "height")):
                selected_region = region
                print("[DEBUG] Valid region, saving:", selected_region)
                save_region(selected_region)
                update_region_display(selected_region)
                set_status("Region selected and saved.")
            else:
                print("[DEBUG] Region invalid or not selected.")
                set_status("No region selected.")
        except Exception as e:
            print("[ERROR] on_select_region failed:", e)
            set_status("Failed to set region.")



    #view wether a region is selected
    def update_region_display(region):
        if region:
            region_status.set("Region selected ✅")
            preview_button.config(state="normal")
        else:
            region_status.set("No region selected ❌")
            preview_button.config(state="disabled")

    # Show the selected region
    def show_region_preview():
        if not selected_region:
            set_status("No region to preview.")
            return

        set_status("Showing region preview...")
        preview = tk.Toplevel()
        preview.attributes("-topmost", True)
        preview.attributes("-alpha", 0.3)
        preview.overrideredirect(True)
        preview.geometry(f"{selected_region['width']}x{selected_region['height']}+{selected_region['left']}+{selected_region['top']}")
        preview.configure(bg='red')
        preview.after(1500, lambda: (preview.destroy(), set_status("Preview closed.")))


    # Clear the selected region
    def on_clear_region():
        nonlocal selected_region
        selected_region = None
        update_region_display(selected_region)
        from .config import CONFIG_FILE
        import os
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
        set_status("Selection cleared.")


    # Helper function to set status
    def set_status(message):
        status_text.set(message)
        print("[STATUS]", message) 


    # ---- UI Setup ----
    root = tk.Tk()
    status_text = tk.StringVar(value="Ready.")
    status_label = tk.Label(
        root,
        textvariable=status_text,
        anchor="w",
        bg="#1e1e1e",
        fg="#aaaaaa",
        relief="sunken",
        font=("Segoe UI", 10)
    )

    status_label.pack(side="bottom", fill="x", padx=5, pady=5)

    root.title("Deadlock Helper")

    width, height = 400, 600
    x, y = monitor.x + 100, monitor.y + 100
    root.geometry(f"{width}x{height}+{x}+{y}")
    # 🔹 Apply dark theme
    root.configure(bg="#2c2c2c")  # dark background

    # 🔹 Define color variables
    fg_color = "#f0f0f0"
    btn_bg = "#444"
    btn_active = "#666"
    font_main = ("Segoe UI", 14)
    font_title = ("Segoe UI", 18, "bold")


    tk.Label(root, text="Deadlock Helper", font=font_title).pack(pady=(20, 10))
    
    
    tk.Button(
        root,
        text="Select Region",
        command=on_select_region,
        font=font_main,
        bg=btn_bg,
        fg=fg_color,
        activebackground=btn_active,
        activeforeground="white",
        relief="flat",
        bd=0
    ).pack(pady=10)

    region_status = tk.StringVar()
    region_label = tk.Label(root, textvariable=region_status)
    region_label.pack(pady=5)

    preview_button = tk.Button(
                            root, 
                            text="Preview Region", 
                            font=font_main, 
                            command=show_region_preview, 
                            state="disabled",
                            bg=btn_bg,
                            fg=fg_color,
                            activebackground=btn_active,
                            activeforeground="white",
                            relief="flat",
                            bd=0
                        )
    preview_button.pack(pady=5)

    tk.Button(
            root, 
            text="Clear Selection", 
            font=font_main, 
            command=on_clear_region,
            bg=btn_bg,
            fg=fg_color,
            activebackground=btn_active,
            activeforeground="white",
            relief="flat",
            bd=0
    ).pack(pady=5)


    tk.Button(
        root, 
        text="Exit", 
        font=font_main, 
        command=root.destroy,
        bg=btn_bg,
        fg=fg_color,
        activebackground=btn_active,
        activeforeground="white",
        relief="flat",
        bd=0
    ).pack(pady=20)

    update_region_display(selected_region)

    update_region_display(selected_region)
    if selected_region:
        set_status("Region loaded from config.")
    else:
        set_status("No region loaded.")


    root.mainloop()