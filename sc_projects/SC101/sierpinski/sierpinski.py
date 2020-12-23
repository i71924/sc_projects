"""
File: sierpinski.py
Name: Po Kai Feng
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Use a recursive function to draw Sierpinski Triangle
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)
	# print(recur_count)   # Count how many times recursion occurs.


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the order of Sierpinski Triangle
	:param length: int(or float), length of the line should be added on window
	:param upper_left_x: int(or float), x0 of the line should be added on window
	:param upper_left_y: int(or float), y0 of the line should be added on window
	This function doesn't return, just draw lines to make up triangles.
	(Only start drawing when order==1)
	"""
	if order < 1:
		# Error case, print message to notice user :)
		print('No orders below 1! :(')
	elif order == 1:
		# Base case: start drawing a triangle
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		line2 = GLine(upper_left_x, upper_left_y, upper_left_x + length / 2, upper_left_y + length * 0.886)
		line3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length / 2, upper_left_y + length * 0.886)
		window.add(line1)
		window.add(line2)
		window.add(line3)
		pause(100)       # Reserved if user need to watch the whole drawing process
	else:
		# Recursive case
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		sierpinski_triangle(order-1, length/2, upper_left_x+length/4, upper_left_y+length/2*0.886)


if __name__ == '__main__':
	main()
