# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv

import numpy as np
from dip import *

class Filtering:

    def __init__(self, image):
        """initializes the variables for frequency filtering on an input image
        takes as input:
        image: the input image
        """
        self.image = image
        self.mask = self.get_mask

    def get_mask(self, shape):
        """Computes a user-defined mask
        takes as input:
        shape: the shape of the mask to be generated
        rtype: a 2d numpy array with size of shape
        """
        mask = np.ones(shape, dtype=np.uint8)
        noise_ranges = [
            ((275, 294), (202, 225)),
            ((240, 249), (230, 242)),
            ((265, 274), (272, 282)),
            ((222, 241), (289, 310))
        ]

        # Apply noise by setting specific regions to 0
        for x, y in noise_ranges:
            mask[x[0]:x[1], y[0]:y[1]] = 0

        return mask

    def post_process_image(self, image):
        """Post processing to display DFTs and IDFTs
        takes as input:
        image: the image obtained from the inverse fourier transform, forward fourier transform, or filtered fourier transform 
        return an image with full contrast stretch
        -----------------------------------------------------
        You can perform post processing as needed. For example,
        1. You can perfrom log compression
        2. You can perfrom a full contrast stretch (fsimage)
        3. You can take negative (255 - fsimage)
        4. etc.
        """
        #use log compression
        log_compression = np.log(1 + image) * 10
        return log_compression

    def filter(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering
        ----------------------------------------------------------
        You are allowed to use inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do post processing on the magnitude and depending on the algorithm (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8
        """
        shifted_dft = fftshift(fft2(self.image))
        mag_dft_compressed = self.post_process_image(np.abs(shifted_dft)).astype('uint8')
        mask = self.get_mask(mag_dft_compressed.shape)
        filtered_dft = mag_dft_compressed * mask

        # Reverse compression
        mag_restored_dft = np.exp(filtered_dft / 10) - 1

        # Get original DFT coefficients
        restored_dft = mag_restored_dft * np.exp(1j * np.angle(shifted_dft))
        restored_image = ifft2(ifftshift(restored_dft)).real

        return [restored_image, mag_dft_compressed, filtered_dft]
