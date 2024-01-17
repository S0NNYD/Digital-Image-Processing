[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/WndnBuLY)
# Digital Image Processing 
Assignment #2


Due: 10/17/23 11:59 PM
__________________________________________________________________________________________________________________
1. (70 Pts) Region Counting:

 	a. (15 Pts) Write a program to binarize a gray-level image based on the assumption that the image has a bimodal histogram.  You are to implement Otsu's thresholding method to estimate the optimal threshold required to binarize the image. Compute Intra-class variance using various thresholds and choose the one that minimizes this value. Your code should report both the binarized image and the optimal threshold value. Also, assume that foreground objects are darker than background objects in the input gray-level image.
	- Starter code available in directory region_analysis/
	- region_analysis/binary_image.py:
		- compute_histogram: write your code to compute the histogram in this function, If you return a list it will automatically save the graph in the output folder
		- find_otsu_threshold: Write your code to compute the optimal threshold using Otsu's method.
		- binarize: write your code to threshold the input image to create a binary image here. This function should return a binary image which will automatically be saved in the output folder. For visualization, one can use an intensity value of 255 instead of 0 in the binary image and 0 instead of 1 in binary images. That way the objects appear black over a white background
	- Any output images or files must be saved to the "output/cellct" folder
  
 	b. (40 Pts) Write a program to perform blobcoloring. The input to your code should be a binary image (0's, and 255's) and the output should be a list of objects or regions in the image. 
	- region_analysis/cell_counting.py:
    	- blob_coloring: write your code for blob coloring here, take as input a binary image, and return a list/dictionary of objects or regions.
	- Any output images or files must be saved to "output/cellct" folder
  
 	c. (15 Pts) Ignore cells smaller than 15 pixels in the area and generate a report of the remaining cells (Cell Number, Area, Location)
	- region_analysis/cell_counting.py:
		- compute_statistics: write your code for computing the statistics of each object/region, i.e. area and location (centroid) here. Print out the statistics to stdout (using the print function; print one row for each region). 
		- Example: region number, area, and centroid (Region: 1, Area: 1000, Centroid: (10,22))
		- mark_image_regions: write your code to create a final cell labeled image. The final image should include an asterisk representing the centroid of each cell and two numbers, one representing its cell number and another its area. Please see the sample output below. To write text on an image, **you are allowed to use the function putText() and FONT_HERSHEY_SIMPLEX in dip.py**.
	

___________________________________________________________________________________________________________________
2. (30 Pts) Image Compression:

	Write a code to compress a binary image using Run length Encoding. 
	- Starter code is available in directory Compression/
	- Compression/run_length_encoding.py
		- encode_image: Write your code to compute the run-length code for the binary image. The input to your function will be a binary image (0s and 255s) and the output is a run-length code.
		- decode_image: Write your code to recover the binary image from the run-length code returned by the encode_image function. The input of the function is the run-length code, height, and width of the binary image The output of the function is the binary image reconstructed from run-length code.
	- Any output image or files must be saved to the "output/Compression" Folder
	 
____________________________________________________________________________________________________________________

**Note:**
We are **restricted from importing cv2, numpy, stats, and other third-party libraries,** 
with the only exception of math, importing math library is allowed (import math).

While you can import it for testing purposes, the final submission should not contain the following statements.
- import cv2
- import numpy
- import numpy as np
- import stats
- etc...

The essential functions for the assignment are available in the dip module one can import using the following statement
```
import dip
from dip import *
```
The following functions are available

```commandline
from cv2 import namedWindow, imshow, waitKey, imwrite, imread, putText, FONT_HERSHEY_SIMPLEX

from numpy import zeros, ones, array, shape, arange
from numpy import random
from numpy import min, max
from numpy import int, uint8, float, complex
from numpy import inf
from numpy.fft import fft2
```

*Assignments that contain any files that import these libraries will not be graded.* 
*Assignments that modify the dip.py file will not be graded.*
		

How to run your code?


  - Usage: ./dip_hw2_region_analysis.py -i image-name
       - image-name: name of the image
  - example: ./dip_hw2_region_analysis.py -i cells.png
  - Please make sure your code runs when you run the above command from the prompt
  - Any output images or files must be saved to "output/" folder
  
  ![Alt text](result.png?raw=true "Sample output")
  - image is provided for testing: cells.png 
  
PS. Files not to be changed: requirements.txt and jenkinsfile directory 

----------------------

Please make sure that your code is running without errors on Jenkins CI/CD.

1. Region Counting - 70 Pts. 
2. Compression     - 30 Pts.

    Total          - 100 Pts.
_______________________________________________________________________________________________________________________

<sub><sup>License: Property of Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston.
This software is the property of the QIL, and should not be distributed, reproduced, or shared online, without the permission of the author
This software is intended to be used by students of the digital image processing course offered at the University of Houston.
The contents are not to be reproduced and shared with anyone without the permission of the author.
The contents are not to be posted on any online public hosting websites without the permission of the author.
The software is cloned and is available to the students for the duration of the course.
At the end of the semester, the GitHub organization is reset, and hence all the existing repositories are reset/deleted, to accommodate the next batch of students.</sub></sup>
