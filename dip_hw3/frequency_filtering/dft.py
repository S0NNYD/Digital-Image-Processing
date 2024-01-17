# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
from dip import *
import math

class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        result = zeros(matrix.shape, dtype=complex)
        for u in range(matrix.shape[0]):
            for v in range(matrix.shape[1]):
                for i in range(matrix.shape[0]):
                    for j in range(matrix.shape[1]):
                        result[u][v] = result[u][v] + matrix[i][j] * (math.cos(2 * math.pi * (u * i + v * j) / 15) - 1J * math.sin(2 * math.pi * (u * i + v * j) / 15))
        return result

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        You can implement the inverse transform formula with or without the normalizing factor.
        Both formulas are accepted.
        takes as input:
        matrix: a 2d matrix (DFT) usually complex
        returns a complex matrix representing the inverse fourier transform"""
        result = zeros(matrix.shape, dtype=complex)
        for u in range(matrix.shape[0]):
            for v in range(matrix.shape[1]):
                for i in range(matrix.shape[0]):
                    for j in range(matrix.shape[1]):
                        result[u][v] = result[u][v] + matrix[i][j] * (math.cos(2 * math.pi * (u * i + v * j) / 15) + 1J * math.sin(2 * math.pi * (u * i + v * j) / 15))
                result[u][v] = result[u][v] / (matrix.shape[0] * matrix.shape[1])
        return result

    def magnitude(self, matrix):
        """Computes the magnitude of the input matrix (iDFT)
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the complex matrix"""
        result = zeros(matrix.shape, dtype=int)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                real = matrix[i][j].real
                img = matrix[i][j].imag

                dist = math.sqrt(real ** 2 + img ** 2)
                result[i][j] = round(dist)
        return result