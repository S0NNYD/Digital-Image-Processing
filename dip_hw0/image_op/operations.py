import math
from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def flip(self, image, direction="horizontal"):
        """
          Perform image flipping along horizontal or vertical direction

          image: the input image to flip
          direction: direction along which to flip

          return: output_image
          """
        # create image with same size as input image
        output_image = zeros(image.shape, dtype=uint8)

        # if direction is horizontal flip along x-axis (columns)
        if direction == "horizontal":
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    output_image[i, j] = image[i, image.shape[1]-1-j]

        # if direction is vertical flip along y-axis (rows)
        if direction == "vertical":
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    output_image[i, j] = image[image.shape[0]-1-i, j]

        return output_image


    def chroma_keying(self, foreground, background, target_color, threshold):
        """
        Perform chroma keying to create an image where the targeted green pixels is replaced with
        background

        foreground_img: the input image with green background
        background_img: the input image with normal background
        target_color: the target color to be extracted (green)
        threshold: value to threshold the pixel proximity to the target color

        return: output_image
        """

        # add your code here
        # Please do not change the structure

        # create image with same size as foreground
        output_image = zeros(foreground.shape, dtype=uint8)

        # loop through the image
        for i in range(foreground.shape[0]):
            for j in range(foreground.shape[1]):
                # check if the pixel is close to the target color
                euclidean_dist = sqrt((foreground[i, j, 0]-target_color[0])**2 + (foreground[i, j, 1]-target_color[1])**2 + (foreground[i, j, 2]-target_color[2])**2)
                if euclidean_dist < threshold:
                    # if close to target color, replace with background
                    output_image[i, j] = background[i, j]
                else:
                    # else keep the foreground
                    output_image[i, j] = foreground[i, j]

        return output_image


