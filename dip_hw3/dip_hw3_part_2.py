"""dip_hw3_part_1.py: Starter file to run howework 3"""
import cv2
from spatial_filtering import filtering

# Example Usage: ./dip_hw3_part_2
# Example Usage: python dip_hw3_part_2.py

__author__      = "Zhenggang Li"
__email__ = "zli36@uh.edu"
__version__ = "1.0.0"


def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def main():
    """ The main funtion that parses input arguments, calls the approrpiate
     fitlering method and writes the output image"""

    # Gaussian
    image_name = "lenna"
    input_image = cv2.imread("Lenna_with_noise.jpg", 0)

    linear_filtering_obj = filtering.Filtering(input_image)

    # Perform Filtering using a Gaussian 5X5 Filter
    smoothed_image = linear_filtering_obj.filter("gaussian")

    output_dir = 'output/'
    output_image_name = output_dir + image_name + "_gaussian.jpg"
    cv2.imwrite(output_image_name, smoothed_image)

    # Laplacian
    image_name = "lenna"
    input_image = cv2.imread("Lenna.png", 0)

    linear_filtering_obj = filtering.Filtering(input_image)

    # Perform filtering using a Laplacian 3X3 filter
    sharpened_image = linear_filtering_obj.filter("laplacian")

    # Write output file
    output_image_name = output_dir + image_name+"_laplacian.jpg"
    cv2.imwrite(output_image_name, sharpened_image)


if __name__ == "__main__":
    main()






