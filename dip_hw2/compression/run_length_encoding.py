import numpy as np
from dip import *
class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        # encode the image
        rle_code = []
        rows, cols = binary_image.shape

        for i in range(rows):
            reference_pixel = binary_image[i, 0]
            rle_code.append(str(binary_image[i, 0]))
            count = 0
            for j in range(cols):
                if binary_image[i, j] == reference_pixel:
                    count += 1
                else:
                    rle_code.append(count)
                    reference_pixel = binary_image[i, j]
                    count = 1
            rle_code.append(count)

        return rle_code

    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        # decode the image
        img = []
        a = 0
        for i in rle_code:
            if i == '255':
                a = 1
            elif i == '0':
                a = 0
            elif a == 0:
                a = 1
                temp = zeros(i, dtype=int)
                img.extend(temp)
            else:
                a = 0
                temp = ones(i, dtype=int) * 255
                img.extend(temp)

        decoded_img = array(img).reshape(height, width)
        return decoded_img










