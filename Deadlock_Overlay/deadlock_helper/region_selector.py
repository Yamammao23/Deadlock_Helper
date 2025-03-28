import tkinter as tk

def select_region():
    region = {}

    def on_mouse_down(event):
        region['start_x'] = selector.winfo_pointerx()
        region['start_y'] = selector.winfo_pointery()
        canvas.coords(rect, region['start_x'], region['start_y'],
                      region['start_x'], region['start_y'])

    def on_mouse_drag(event):
        x, y = selector.winfo_pointerx(), selector.winfo_pointery()
        canvas.coords(rect, region['start_x'], region['start_y'], x, y)

    def on_mouse_up(event):
        print("[DEBUG] Mouse released.")
        coords = canvas.coords(rect)
        print(f"[DEBUG] Rectangle coords: {coords}")
        if len(coords) != 4:
            print("[ERROR] Unexpected number of coordinates returned.")
            selector.destroy()
            return

        x1, y1, x2, y2 = coords

        if x1 == x2 or y1 == y2:
            print("[DEBUG] Region was not drawn — zero width or height.")
            selector.destroy()
            return

        region.update({
            'left': int(min(x1, x2)),
            'top': int(min(y1, y2)),
            'width': int(abs(x2 - x1)),
            'height': int(abs(y2 - y1))
        })
        print(f"[DEBUG] Region finalized: {region}")
        selector.quit()

    print("[DEBUG] Starting region selector...")

    selector = tk.Tk()
    selector.attributes("-fullscreen", True)
    selector.attributes("-alpha", 0.3)
    selector.configure(bg='black')
    selector.title("Select region")

    canvas = tk.Canvas(selector, bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    rect = canvas.create_rectangle(0, 0, 0, 0, outline="red", width=2, fill="red")

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    selector.mainloop()
    selector.destroy()

    print(f"[DEBUG] Region after selector close: {region}")
    if all(k in region for k in ('left', 'top', 'width', 'height')):
        return region
    else:
        print("[DEBUG] No region was returned.")
        return None
