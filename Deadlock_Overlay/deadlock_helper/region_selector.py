
import tkinter as tk

def select_region():
    region = {}

    def on_mouse_down(event):
        region['start_x'] = root.winfo_pointerx()
        region['start_y'] = root.winfo_pointery()
        canvas.coords(rect, region['start_x'], region['start_y'],
                      region['start_x'], region['start_y'])

    def on_mouse_drag(event):
        x, y = root.winfo_pointerx(), root.winfo_pointery()
        canvas.coords(rect, region['start_x'], region['start_y'], x, y)

    def on_mouse_up(event):
        x1, y1, x2, y2 = canvas.coords(rect)
        region.update({
            'left': int(min(x1, x2)),
            'top': int(min(y1, y2)),
            'width': int(abs(x2 - x1)),
            'height': int(abs(y2 - y1))
        })
        root.destroy()

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.3)
    root.configure(bg='black')
    root.title("Select region")

    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    rect = canvas.create_rectangle(0, 0, 0, 0, outline="red", width=2, fill="red")

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    root.mainloop()
    return region if 'left' in region else None
