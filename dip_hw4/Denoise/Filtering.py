import math
from dip import *
class Filtering:

    def __init__(self, image, filter_name, filter_size, var = None):
        """initializes the variables of spatial filtering on an input image
        takes as input:
        image: the noisy input image
        filter_name: the name of the filter to use
        filter_size: integer value of the size of the fitler
        
        """

        self.image = image

        if filter_name == 'arithmetic_mean':
            self.filter = self.get_arithmetic_mean
        elif filter_name == 'geometric_mean':
            self.filter = self.get_geometric_mean
        if filter_name == 'local_noise':
            self.filter = self.get_local_noise
        elif filter_name == 'median':
            self.filter = self.get_median
        elif filter_name == 'adaptive_median':
            self.filter = self.get_adaptive_median

        self.filter_size = filter_size
        
        # global_var: noise variance to be used in the Local noise reduction filter        
        self.global_var = var
        
        # S_max: Maximum allowed size of the window that is used in the adaptive median filter
        self.S_max = 15

    def get_arithmetic_mean(self, roi):
        """Computes the arithmetic mean of the input ROI
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the arithmetic mean value of the roi"""

        result = 0
        for i in range(len(roi)):
            result += roi[i]
        result /= len(roi)

        return result

    def get_geometric_mean(self, roi):
        """Computes the geometric mean for the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the geometric mean value of the roi"""

        result = 1
        for i in range(len(roi)):
            result *= roi[i]
        result = result ** (1 / len(roi))

        return result

    def get_local_noise(self, roi):
        """Computes the local noise reduction value
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the local noise reduction value of the roi"""

        local_mean = sum(roi) / len(roi)
        local_var = 0
        for i in roi:
            local_var += (i - local_mean) ** 2
        local_var /= len(roi)

        if local_var == 0:
            return local_mean
        else:
            mid = len(roi) // 2
            mean = roi[mid] - local_mean
            result = (1 / local_var) * mean
            return result

    def get_median(self, roi):
        """Computes the median for the input roi
        takes as input:
        roi: region of interest (a list/array of intensity values)
        returns the median value of the roi
        Do not use any in-built median function from numpy or other libraries.
        """
        roi = sorted(roi)
        result = 0
        if len(roi) % 2 == 0:
            result = (roi[len(roi) // 2] + roi[len(roi) // 2 - 1]) / 2
        else:
            result = roi[int(len(roi) // 2)]
        return result


    def get_adaptive_median(self, pad_image, curr_row, curr_col, roi, window_size):
        """Use this function to implement the adaptive median.
        It is left up to the student to define the input to this function and call it as needed. Feel free to create
        additional functions as needed.
        """
        min_z = min(roi)
        max_z = max(roi)

        roi = sorted(roi)
        length = len(roi)
        mid = length // 2

        if length % 2 == 0:
            median = (roi[mid - 1] + roi[mid]) / 2
        else:
            median = roi[mid]

        median_z = median
        var1 = median_z - min_z
        var2 = median_z - max_z

        if var1 > 0 > var2:
            b1 = pad_image[curr_row][curr_col] - min_z
            b2 = pad_image[curr_row][curr_col] - max_z

            if b1 > 0 > b2:
                return pad_image[curr_row][curr_col]
            else:
                return median_z
        else:
            window_size += 1

            if window_size < 16:
                updated_roi = []
                padding = window_size // 2

                for x in range(window_size):
                    for y in range(window_size):
                        updated_roi.append(pad_image[curr_row - padding + x][curr_col - padding + y])

                return self.get_adaptive_median(pad_image, curr_row, curr_col, updated_roi, window_size)
            else:
                return median_z


    def filtering(self):
        """performs filtering on an image containing Gaussian or salt & pepper noise
        returns the denoised image
        ----------------------------------------------------------
        Note: Here when we perform filtering we are not doing convolution.
        For every pixel in the image, we select a neighborhood of values defined by the kernel and apply a mathematical
        operation for all the elements within the kernel. For example, mean, median, etc.

        Steps:
        1. add the necessary zero padding to the noisy image, that way we have sufficient values to perform the operations on the pixels at the image corners. The number of rows and columns of zero padding is defined by the kernel size
        2. Iterate through the image and for every pixel (i,j) gather the neighbors defined by the kernel into a list (or any data structure)
        3. Pass these values to one of the filters that will compute the necessary mathematical operations (mean, median, etc.)
        4. Save the results at (i,j) in the output image.
        5. return the output image

        Note: You can create extra functions as needed. For example, if you feel that it is easier to create a new function for
        the adaptive median filter as it has two stages, you are welcome to do that.
        For the adaptive median filter assume that S_max (maximum allowed size of the window) is 15
        """
        if self.filter == self.get_local_noise:
            pad_size = self.filter_size // 2
            padded_image = zeros((self.image.shape[0] + 2 * pad_size, self.image.shape[1] + 2 * pad_size))
            padded_image[pad_size:-pad_size, pad_size:-pad_size] = self.image
            output_image = zeros(self.image.shape)
            mean = sum(self.image) / len(self.image)

            for i in range(pad_size, padded_image.shape[0] - pad_size):
                for j in range(pad_size, padded_image.shape[1] - pad_size):
                    roi = []
                    for x in range(self.filter_size):
                        for y in range(self.filter_size):
                            roi.append(padded_image[i - pad_size + x][j - pad_size + y])
                    mean = self.filter(roi)
                    g_x = padded_image[i][j]
                    mean = g_x - self.global_var * mean
                    output_image[i - pad_size][j - pad_size] = mean

            return output_image

        if self.filter == self.get_adaptive_median:
            pad_size = 15 // 2
            padded_image = zeros((self.image.shape[0] + 2 * pad_size, self.image.shape[1] + 2 * pad_size))
            for i in range(pad_size, padded_image.shape[0] - pad_size):
                for j in range(pad_size, padded_image.shape[1] - pad_size):
                    padded_image[i][j] = self.image[i - pad_size][j - pad_size]

            window_size = self.filter_size
            output_image = zeros(self.image.shape)
            for i in range(pad_size, padded_image.shape[0] - pad_size):
                for j in range(pad_size, padded_image.shape[1] - pad_size):
                    roi = []
                    for x in range(window_size):
                        for y in range(window_size):
                            roi.append(padded_image[i - window_size + x][j - window_size + y])
                    output_image[i - pad_size][j - pad_size] = self.filter(padded_image, i, j, roi, window_size)

            return output_image
        else:
            pad_size = self.filter_size // 2
            output_image = zeros(self.image.shape)
            padded_image = zeros((self.image.shape[0] + 2 * pad_size, self.image.shape[1] + 2 * pad_size))
            padded_image[pad_size:-pad_size, pad_size:-pad_size] = self.image

            for i in range(pad_size, padded_image.shape[0] - pad_size):
                for j in range(pad_size, padded_image.shape[1] - pad_size):
                    roi = []
                    for x in range(self.filter_size):
                        for y in range(self.filter_size):
                            roi.append(padded_image[i - pad_size + x][j - pad_size + y])
                    output_image[i - pad_size][j - pad_size] = self.filter(roi)

            return output_image

