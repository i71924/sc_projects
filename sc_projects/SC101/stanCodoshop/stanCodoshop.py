"""
File: stanCodoshop.py
Name: Po Kai Feng
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value
    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images
    Returns:
        dist^(1/2)(float): color distance between red, green, and blue pixel values
    """
    # red_dist_sqr = (pixel.red-red)*(pixel.red-red)
    # green_dist_sqr = (pixel.green-green)*(pixel.green-green)
    # blue_dist_sqr = (pixel.blue-blue)*(pixel.blue-blue)
    # dist_sqr = red_dist_sqr + green_dist_sqr + blue_dist_sqr
    return ((pixel.red-red)*(pixel.red-red)+(pixel.green-green)*(pixel.green-green)+(pixel.blue-blue)*(pixel.blue-blue))**0.5


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values
    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively
        returning in the order: [red, green, blue]
    """
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    for i in range(len(pixels)):
        red_sum += pixels[i].red
        green_sum += pixels[i].green
        blue_sum += pixels[i].blue
    rgb = [red_sum//len(pixels), green_sum//len(pixels), blue_sum//len(pixels)]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.
    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        (Pixel): pixel closest to RGB averages
    """
    index = 0
    min_dist = get_pixel_dist(pixels[0], get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])
    for i in range(1, len(pixels)):
        if min_dist >= get_pixel_dist(pixels[i], get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2]):
            min_dist = get_pixel_dist(pixels[i], get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])
            index = i
            # identify the pixel which has the minimun color distance to the average color
    return pixels[index]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.
    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    pixels = []
    # list to contain all the pixels in the image
    for i in range(width):
        for j in range(height):
            for k in range(len(images)):
                # images[k].make_as_big_as(images[0])
                # To make sure all the list of images have same size thus they can be compared with same pixels
                pixels.append(images[k].get_pixel(i, j))
                # Get the pixels of all images at (i, j)
            best_pix = get_best_pixel(pixels)
            result_pix = result.get_pixel(i, j)
            result_pix.red = best_pix.red
            result_pix.green = best_pix.green
            result_pix.blue = best_pix.blue
            pixels = []
            # Re-assign to void list
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
