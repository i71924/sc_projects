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
            pixel = img.get_pixel(x, y)
            blur_pixel = blur_img.get_pixel(x, y)
            # Divided into 9 conditions
            if x == 0:
                if y == 0:
                    pixel1 = img.get_pixel(x+1, y)
                    pixel2 = img.get_pixel(x, y+1)
                    pixel3 = img.get_pixel(x+1, y+1)
                    blur_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red) // 4
                    blur_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green) // 4
                    blur_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue) // 4
                elif y < img.height - 1:
                    pixel1 = img.get_pixel(x, y-1)
                    pixel2 = img.get_pixel(x+1, y-1)
                    pixel3 = img.get_pixel(x+1, y)
                    pixel4 = img.get_pixel(x, y+1)
                    pixel5 = img.get_pixel(x+1, y+1)
                    blur_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red) // 6
                    blur_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green) // 6
                    blur_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue) // 6
                else:
                    # y == img.height-1
                    pixel1 = img.get_pixel(x, y-1)
                    pixel2 = img.get_pixel(x+1, y-1)
                    pixel3 = img.get_pixel(x+1, y)
                    blur_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red) // 4
                    blur_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green) // 4
                    blur_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue) // 4
            elif x < img.width - 1:
                if y == 0:
                    pixel1 = img.get_pixel(x-1, y)
                    pixel2 = img.get_pixel(x+1, y)
                    pixel3 = img.get_pixel(x-1, y+1)
                    pixel4 = img.get_pixel(x, y+1)
                    pixel5 = img.get_pixel(x+1, y+1)
                    blur_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red) // 6
                    blur_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green) // 6
                    blur_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue) // 6
                elif y < img.height - 1:
                    pixel1 = img.get_pixel(x-1, y-1)
                    pixel2 = img.get_pixel(x, y-1)
                    pixel3 = img.get_pixel(x+1, y-1)
                    pixel4 = img.get_pixel(x-1, y)
                    pixel5 = img.get_pixel(x+1, y)
                    pixel6 = img.get_pixel(x-1, y+1)
                    pixel7 = img.get_pixel(x, y+1)
                    pixel8 = img.get_pixel(x+1, y+1)
                    blur_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red + pixel6.red + pixel7.red + pixel8.red) // 9
                    blur_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green + pixel6.green + pixel7.green + pixel8.green) // 9
                    blur_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue + pixel6.blue + pixel7.blue + pixel8.blue) // 9
                else:
                    # y == img.height-1
                    pixel1 = img.get_pixel(x-1, y-1)
                    pixel2 = img.get_pixel(x, y-1)
                    pixel3 = img.get_pixel(x+1, y-1)
                    pixel4 = img.get_pixel(x-1, y)
                    pixel5 = img.get_pixel(x+1, y)
                    blur_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red) // 6
                    blur_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green) // 6
                    blur_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue) // 6
            else:
                # x == img.width - 1
                if y == 0:
                    pixel1 = img.get_pixel(x-1, y)
                    pixel2 = img.get_pixel(x-1, y+1)
                    pixel3 = img.get_pixel(x, y+1)
                    blur_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red) // 4
                    blur_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green) // 4
                    blur_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue) // 4
                elif y < img.height - 1:
                    pixel1 = img.get_pixel(x-1, y-1)
                    pixel2 = img.get_pixel(x, y-1)
                    pixel3 = img.get_pixel(x-1, y)
                    pixel4 = img.get_pixel(x-1, y+1)
                    pixel5 = img.get_pixel(x, y+1)
                    blur_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel5.red) // 6
                    blur_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel5.green) // 6
                    blur_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel5.blue) // 6
                else:
                    # y == img.height-1
                    pixel1 = img.get_pixel(x-1, y-1)
                    pixel2 = img.get_pixel(x, y-1)
                    pixel3 = img.get_pixel(x-1, y)
                    blur_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red) // 4
                    blur_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green) // 4
                    blur_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue) // 4
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
