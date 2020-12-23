"""
File: shrink.py
Name: Po Kai Feng
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the location of the picture
    :return: img, the shrink picture
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank((img.width+1) // 2, (img.height+1) // 2)
    for x in range(0, img.width, 2):
        for y in range(0, img.height, 2):
            pixel = img.get_pixel(x, y)
            new_pixel = new_img.get_pixel(x//2, y//2)
            """
            For every pixel(x, y) in img, assigns the average RGB of pixel(x, y), pixel(x+1, y),
            pixel(x, y+1) and pixel(x+1, y+1) to new_pixel(x//2, y//2) in new_img.
            """
            if ((img.width+1) % 2 == 0 and x == img.width - 1) or ((img.height + 1) % 2 == 0 and y == img.height - 1):
                # It's the end of img.width or img.height.
                new_pixel.red = pixel.red
                new_pixel.green = pixel.green
                new_pixel.blue = pixel.blue
            else:
                pixel1 = img.get_pixel(x+1, y)
                pixel2 = img.get_pixel(x, y+1)
                pixel3 = img.get_pixel(x, y+1)
                new_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red) // 4
                new_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green) // 4
                new_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue) // 4
    return new_img


def main():
    """
    First show the original picture. Then show the shrinked picture.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
