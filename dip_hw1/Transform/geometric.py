from .interpolation import interpolation
from dip import *
import math
"""
Do not import cv2, numpy and other third party libs
"""


class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):
        """Computes the forward rotated image by an angle theta
                image: input image
                theta: angle to rotate the image by (in radians)
                return the rotated image"""
        # 1. make rotation matrix
        rotation_matrix = array([[math.cos(theta), -math.sin(theta)],
                                 [math.sin(theta), math.cos(theta)]])

        # 2. rotate corners
        corners = {"top_left": array([0, 0]),
                   "top_right": array([0, image.shape[1]]),
                   "bottom_left": array([image.shape[0], 0]),
                   "bottom_right": array([image.shape[0], image.shape[1]])}
        transformed_corners = dict()
        min_x, min_y = inf, inf
        max_x, max_y = -inf, -inf
        for i in corners:
            transformed_corners[i] = sum(rotation_matrix * corners[i], axis=1)
            if transformed_corners[i][0] < min_x:
                min_x = transformed_corners[i][0]
            if transformed_corners[i][1] < min_y:
                min_y = transformed_corners[i][1]
            if transformed_corners[i][0] > max_x:
                max_x = transformed_corners[i][0]
            if transformed_corners[i][1] > max_y:
                max_y = transformed_corners[i][1]

        # 3. create rotated image               rows                cols
        rotated_image = zeros((int(max_x - min_x), int(max_y - min_y)), dtype=uint8)

        # 4. for each (i,j) in original image
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                # compute rotated location (i', j')
                compute_i = i * rotation_matrix[0][0] + j * rotation_matrix[0][1]
                compute_j = i * rotation_matrix[1][0] + j * rotation_matrix[1][1]

                # i'_n = i' - min_x, j'_n = j' - min_y
                i_apostrophe_n = int(compute_i - min_x)
                j_apostrophe_n = int(compute_j - min_y)

                # check if in bounds R(i'_n, j'_n) = I(i, j)
                if rotated_image.shape[0] > i_apostrophe_n >= 0 and rotated_image.shape[1] > j_apostrophe_n >= 0:
                    rotated_image[i_apostrophe_n][j_apostrophe_n] = image[i][j]

        return rotated_image


    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        """Computes the reverse rotated image by an angle theta
                rotated_image: the rotated image from previous step
                theta: angle to rotate the image by (in radians)
                Origin: origin of the original image with respect to the rotated image
                Original shape: Shape of the orginal image
                return the original image"""

        # 1. make inverse rotation matrix
        inverse_rotation_matrix = array([[math.cos(theta), math.sin(theta)],
                                         [-math.sin(theta), math.cos(theta)]])

        # 2. create image of original shape
        reverse_rotated_image = zeros(original_shape, dtype=uint8)

        # 3. for each (i'_n, j'_n) in rotated image
        for i_apostrophe_n in range(rotated_image.shape[0]):
            for j_apostrophe_n in range(rotated_image.shape[1]):
                # compute location with respect to O
                compute_i = i_apostrophe_n - origin[0]
                compute_j = j_apostrophe_n - origin[1]

                # compute inverse rotation on (i', j') to get (i, j)
                i = int(compute_i * inverse_rotation_matrix[0][0] + compute_j * inverse_rotation_matrix[0][1])
                j = int(compute_i * inverse_rotation_matrix[1][0] + compute_j * inverse_rotation_matrix[1][1])

                # check if in bounds I(i,j) = R(i'_n, j'_n)
                if original_shape[0] > i >= 0 and original_shape[1] > j >= 0:
                    reverse_rotated_image[i][j] = rotated_image[i_apostrophe_n][j_apostrophe_n]

        return reverse_rotated_image

    def rotate(self, image, theta, interpolation_type):
        """Computes the rotated image by an angle theta and perfrom interpolation
                image: the input image
                theta: angle to rotate the image by (in radians)
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the rotated image"""

        # 1. make rotation matrix
        rotation_matrix = array([[math.cos(theta), -math.sin(theta)],
                                 [math.sin(theta), math.cos(theta)]])

        # 2. make inverse rotation matrix
        inverse_rotation_matrix = array([[math.cos(theta), math.sin(theta)],
                                         [-math.sin(theta), math.cos(theta)]])

        # 3. compute size of rotated image
        corners = {"top_left": array([0, 0]),
                   "top_right": array([0, image.shape[1]]),
                   "bottom_left": array([image.shape[0], 0]),
                   "bottom_right": array([image.shape[0], image.shape[1]])}
        transformed_corners = dict()
        min_x, min_y = inf, inf
        max_x, max_y = -inf, -inf
        for i in corners:
            transformed_corners[i] = sum(rotation_matrix * corners[i], axis=1)
            if transformed_corners[i][0] < min_x:
                min_x = transformed_corners[i][0]
            if transformed_corners[i][1] < min_y:
                min_y = transformed_corners[i][1]
            if transformed_corners[i][0] > max_x:
                max_x = transformed_corners[i][0]
            if transformed_corners[i][1] > max_y:
                max_y = transformed_corners[i][1]

        # 4. create rotated image
        rotated_image = zeros((int(max_x - min_x), int(max_y - min_y)), dtype=uint8)

        # 5. calculate location O with respect to n
        location_ox = int(-min_x)
        location_oy = int(-min_y)

        # implement interpolation for nearest neighbor
        if interpolation_type == "nearest_neighbor":
            # 6. for (i'_n, j'_n) in rotated image
            for i_apostrophe_n in range(rotated_image.shape[0]):
                for j_apostrophe_n in range(rotated_image.shape[1]):
                    # calculate location with respect to O
                    compute_i = i_apostrophe_n - location_ox
                    compute_j = j_apostrophe_n - location_oy

                    # compute inverse rotation on i' and j' to get i and j
                    i = int(compute_i * inverse_rotation_matrix[0][0] + compute_j * inverse_rotation_matrix[0][1])
                    j = int(compute_i * inverse_rotation_matrix[1][0] + compute_j * inverse_rotation_matrix[1][1])

                    # use nearest neighbor
                    i_nn = int(round(i))
                    j_nn = int(round(j))

                    # R(i'_n, j'_n) = I(i_nn, j_nn)
                    if image.shape[0] > i_nn >= 0 and image.shape[1] > j_nn >= 0:
                        rotated_image[i_apostrophe_n][j_apostrophe_n] = image[i_nn][j_nn]

        # implement bilinear interpolation
        if interpolation_type == "bilinear":
            # 6. for (i'_n, j'_n) in rotated image
            for i_apostrophe_n in range(rotated_image.shape[0]):
                for j_apostrophe_n in range(rotated_image.shape[1]):
                    # calculate location with respect to O
                    compute_i = i_apostrophe_n - location_ox
                    compute_j = j_apostrophe_n - location_oy

                    # compute inverse rotation on i' and j' to get i and j
                    i = compute_i * inverse_rotation_matrix[0][0] + compute_j * inverse_rotation_matrix[0][1]
                    j = compute_i * inverse_rotation_matrix[1][0] + compute_j * inverse_rotation_matrix[1][1]

                    # find four nearest neighbors to (i, j)
                    i1 = math.floor(i)
                    i2 = math.ceil(i)
                    j1 = math.floor(j)
                    j2 = math.ceil(j)

                    if 0 < i1 < image.shape[0] and 0 < j1 < image.shape[1] and 0 < i2 < image.shape[0] and 0 < j2 < image.shape[1]:
                        # Calculate the interpolated value using bilinear interpolation
                        pt1 = (i1, j1)
                        pt2 = (i2, j1)
                        pt3 = (i1, j2)
                        pt4 = (i2, j2)

                        i_pt1 = image[i1, j1]
                        i_pt2 = image[i2, j1]
                        i_pt3 = image[i1, j2]
                        i_pt4 = image[i2, j2]

                        intensity = interpolation()
                        interpolated_value = intensity.bilinear_interpolation(pt1, pt2, pt3, pt4, i_pt1, i_pt2, i_pt3, i_pt4, i, j)

                        # Set the interpolated value in the rotated image
                        rotated_image[i_apostrophe_n][j_apostrophe_n] = interpolated_value

        return rotated_image


