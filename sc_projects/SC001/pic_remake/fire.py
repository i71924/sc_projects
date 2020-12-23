"""
File: fire.py
Name: Po Kai Feng
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the location of the original picture which we want to determine
    :return: img, the picture with the fire area being highlighted
    """
    img = SimpleImage(filename)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            pixel_avg = (pixel.red + pixel.green + pixel.blue) // 3
            if pixel.red > pixel_avg * HURDLE_FACTOR:
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.red = pixel_avg
                pixel.green = pixel_avg
                pixel.blue = pixel_avg
    return img


def main():
    """
    First show the original picture. Then highlight the picture's fire area
    and show it again.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
