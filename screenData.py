import tkinter as tk

def select_screen_area(callback):
    """Allows the user to select a screen area interactively using Tkinter."""
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg="gray")
    root.attributes("-alpha", 0.3)  # Make the overlay semi-transparent

    canvas = tk.Canvas(root, cursor="cross", bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    rect = None
    start_x = start_y = 0

    def on_mouse_down(event):
        nonlocal rect, start_x, start_y
        start_x, start_y = event.x, event.y
        rect = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red", width=2)

    def on_mouse_drag(event):
        nonlocal rect
        if rect:
            canvas.coords(rect, start_x, start_y, event.x, event.y)

    def on_mouse_release(event):
        """Capture the selected area and close the window."""
        nonlocal rect
        if rect:
            end_x, end_y = event.x, event.y
            x1, y1 = min(start_x, end_x), min(start_y, end_y)
            x2, y2 = max(start_x, end_x), max(start_y, end_y)
            area = (x1, y1, x2, y2)

            # Send the area to the callback
            callback(area)
            root.destroy()  # Close the selection window

    # Bind mouse events
    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_release)

    root.mainloop()
