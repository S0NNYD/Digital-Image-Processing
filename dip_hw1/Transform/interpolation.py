from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class interpolation:

    def linear_interpolation(self, i1, i2, x, x1, x2):
        """Computes the linear interpolation value at some iD location x between two 1D points (Pt1 and Pt2).

        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.

        The function ideally takes two 1D points Pt1 and Pt2, and their intensitites I(Pt1), I(Pt2).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for linear interpolation here
        result = ((i1 * (x2 - x)) / (x2 - x1)) + ((i2 * (x - x1)) / (x2 - x1))

        return result

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, i_pt1, i_pt2, i_pt3, i_pt4, x, y):
        """Computes the bilinear interpolation value at some 2D location x between four 2D points (Pt1, Pt2, Pt3, and Pt4).

        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.

        The function ideally takes four 2D points Pt1, Pt2, Pt3, and Pt4, and their intensitites I(Pt1), I(Pt2), I(Pt3), and I(Pt4).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for bilinear interpolation here
        # Recall that bilinear interpolation performs linear interpolation three times
        # Please reuse or call linear interpolation method three times by passing the appropriate parameters to compute this task

        ix1 = self.linear_interpolation(i_pt1, i_pt2, x, pt1[0], pt2[0])
        ix2 = self.linear_interpolation(i_pt3, i_pt4, x, pt3[0], pt4[0])

        # Perform linear interpolation in the y-direction using the results from the previous step
        result = self.linear_interpolation(ix1, ix2, y, pt1[1], pt3[1])
        return result
