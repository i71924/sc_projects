"""
File: blur.py
Name: Po Kai Feng
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: img, SimpleImage of the picture
    :return: img, the blurred picture
    """
    blur_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            count = 0
            pixel = img.get_pixel(x, y)
            blur_pixel = blur_img.get_pixel(x, y)
            # Divided into 9 conditions
            for i in range(-1,1):
                for j in range(-1,1):
                    if x+i < 0 or x+i > img.height-1
    return blur_img


def main():
    """
    First show the original picture. Then show the blurred picture.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
