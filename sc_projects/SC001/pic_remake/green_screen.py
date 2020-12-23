"""
File: green_screen.py
Name: Po Kai Feng
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


GREEN_SCREEN = 2
# The factor to determine whether it's green screen.


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, the picture that should be added on background image
    :return: img, the combination of two pictures
    """
    background_img.make_as_big_as(figure_img)
    for x in range(background_img.width):
        for y in range(background_img.height):
            pixel_bg = background_img.get_pixel(x, y)
            pixel_fg = figure_img.get_pixel(x, y)
            bigger = max(pixel_fg.red, pixel_fg.blue)
            if pixel_fg.green > GREEN_SCREEN * bigger:
                pixel_fg.red = pixel_bg.red
                pixel_fg.green = pixel_bg.green
                pixel_fg.blue = pixel_bg.blue
    return figure_img


def main():
    """
    First open the background and the figure pictures. Then combine two pictures and show.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
