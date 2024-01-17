import numpy as np
from dip import *
import math

class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        """Initialzes/Computes and returns a 5X5 Gaussian filter"""
        gaussian_filter = zeros((5, 5))
        sum = 0

        for i in range(5):
            for j in range(5):
                exp = math.exp(-((i - 2) ** 2 + (j - 2) ** 2) / 2)
                eval = math.exp(exp)
                temp = (1 / (2 * math.pi)) * eval
                sum += temp
                gaussian_filter[i][j] = temp
        return gaussian_filter, sum

    def get_laplacian_filter(self):
        """Initialzes and returns a 3X3 Laplacian filter"""
        laplacian_filter = array([[0, -1, 0],
                                  [-1, 4, -1],
                                  [0, -1, 0]])
        return laplacian_filter

    def filter(self, filter_name):
        """Perform filtering on the image using the specified filter, and returns a filtered image
            takes as input:
            filter_name: a string, specifying the type of filter to use ["gaussian", laplacian"]
            return type: a 2d numpy array
                """
        if filter_name == "gaussian":
            gaussian_filter, sum = self.get_gaussian_filter()

            #pad the image
            padded_image = zeros((self.image.shape[0] + 4, self.image.shape[1] + 4))
            padded_image[2:-2, 2:-2] = self.image

            #apply the gaussian filter
            filtered_image = zeros(padded_image.shape)
            for i in range(2, padded_image.shape[0] - 2):
                for j in range(2, padded_image.shape[1] - 2):
                    temp = 0
                    subimg = padded_image[i - 2:i + 3, j - 2:j + 3]
                    for x in range(subimg.shape[0]):
                        for y in range(subimg.shape[1]):
                            temp += subimg[x][y] * gaussian_filter[x][y]
                    filtered_image[i][j] = temp / sum
            return filtered_image[2:-2, 2:-2]

        if filter_name == "laplacian":
            laplacian_filter = self.get_laplacian_filter()

            #pad the image
            padded_image = zeros((self.image.shape[0] + 2, self.image.shape[1] + 2))
            padded_image[1:-1, 1:-1] = self.image

            #apply the laplacian filter
            filtered_image = zeros(padded_image.shape)
            for i in range(1, padded_image.shape[0] - 1):
                for j in range(1, padded_image.shape[1] - 1):
                    temp = 0
                    subimg = padded_image[i - 1:i + 2, j - 1:j + 2]
                    for x in range(subimg.shape[0]):
                        for y in range(subimg.shape[1]):
                            temp += subimg[x][y] * laplacian_filter[x][y]
                    filtered_image[i][j] = temp
            return filtered_image[1:-1, 1:-1]
