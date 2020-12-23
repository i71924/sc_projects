"""
File: draw_line.py
Name: Po Kai Feng
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant
SIZE = 10
# Control the diameter of the round oval
window = GWindow()
has_oval = False
# To show that whether the window has oval in it
x0 = 0
y0 = 0
# The initial location of the line(may be changed by mouseclick)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    """
    Draw an oval at the location of the mouse if there is no oval in the window,
    or draw a line and remove the oval if there is an oval in the window.
    """
    global has_oval, x0, y0
    if not has_oval:
        # There is no oval in the window
        oval = GOval(SIZE, SIZE)
        window.add(oval, mouse.x-SIZE/2, mouse.y-SIZE/2)
        has_oval = not has_oval
        x0 = mouse.x
        y0 = mouse.y
        # Assign the initial location of the line that user wants to draw
    else:
        # There is an oval in the window
        window.remove(window.get_object_at(x0, y0))
        line = GLine(x0, y0, mouse.x, mouse.y)
        window.add(line)
        has_oval = not has_oval


if __name__ == "__main__":
    main()
