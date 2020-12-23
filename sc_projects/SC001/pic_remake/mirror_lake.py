"""
File: mirror_lake.py
Name: Po Kai Feng
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the location of the original picture
    :return: img, the mirrored picture
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width, 2*img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            blank_pixel1 = blank_img.get_pixel(x, y)
            blank_pixel1.red = pixel.red
            blank_pixel1.green = pixel.green
            blank_pixel1.blue = pixel.blue
            blank_pixel2 = blank_img.get_pixel(x, blank_img.height-y-1)
            blank_pixel2.red = pixel.red
            blank_pixel2.green = pixel.green
            blank_pixel2.blue = pixel.blue
    return blank_img


def main():
    """
    First show th original picture. Then show the mirrored picture.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
