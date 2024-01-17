[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/41u6l_yt)
# Digital Image Processing 
Assignment #3

Due: Tue 11/20/23 11:59 PM


1. DFT:
(15 Pts.) Write code for computing the forward Fourier transform, inverse Fourier transform, and magnitude of the Fourier transform. 
The input to your program is a 2D matrix of size 15X15.

  - Starter code available in directory frequency_filtering/
  - dft/Dft.py: Edit the functions "forward_transform", "inverse_transform", and "magnitude", you are welcome to add more functions.
  - For this part of the assignment, please implement your own code for all computations, do not use inbuilt functions - like "fft", "dft", "abs" from numpy, opencv or other libraries - that directly accomplish the objective of the question. You can use functions such as "sin" and "cos" from the math package as needed.   
  - This part of the assignment can be run using dip_hw3_part_1.py (Do Not modify this file)
  - Usage: 
            
        python dip_hw3_part_1.py
  - Please make sure your code runs when you run the above command from prompt/terminal
  - Do not save any output in your code. Any output images or files will be saved to "output/" folder (dip_hw3_part_1.py automatically does this)
  
-------------
2. Linear Filtering:
(30 Pts.) Write code to perform spatial filtering on an image using 5X5 Gaussian filter and a 3X3 Laplacian filter.

  - Starter code available in directory spatial_filtering/
  - spatial_filtering/filtering.py:
    - \__init__(): Will initialize the required variable for filtering (image). DO NOT edit this function.
    - get_gaussian_filter():  Write your code to compute a 5X5 Gaussian filtering here.
    - get_laplacian_filter(): Wring your code to initialize a 3X3 Laplacian filtering here.
    - filter(): Wring your code to perform filtering operation on the input image using the specified filter.
- For this part of the assignment, please implement your own code for all computations, do not use inbuilt functions from numpy, opencv or other libraries that directly accomplish the objective of the question. You can use functions from math package if needed.
  - This part of the assignment can be run using dip_hw3_part_2.py (Do Not modify this file)
  - Usage:

        python dip_hw3_part_2.py
  - Please make sure your code runs when you run the above command from prompt/terminal
  - Do not save any output in your code. Any output images or files will be saved to "output/" folder (dip_hw3_part_2.py automatically does this)

-------------
3. Frequency Filtering:
(30 Pts.) Write code to perform image filtering in the frequency domain. The input image is corrupted with periodic noise.
   To perform filtering:
    1. Compute the DFT of the image.
    2. Inspect the DFT to identify the noise frequencies. 
    3. Create a filter using trial and error to reject the noise frequencies.
    4. Compute the inverse DFT of the filtered frequencies to obtain the filtered image. 
       
The input to your program is an image with periodic noise. 

- Starter code available in directory frequency_filtering/ 
- frequency_filtering/filtering.py:
  - \__init__(): Will initialize the required variable for filtering (image). An addsinNoise function will be called to add sine noise to a given image. DO NOT edit this function.  
  - get_mask: Write your code to generate the masks to reject noise frequencies. 
  - filter(): Write your code to perform image filtering here. The required variables have been initialized and can be used as self.image, self.mask. 
    - The function returns three images, filtered image, magnitude of the DFT, and magnitude of filtered dft 
    - Perform necessary post-processing to make the images visible. (Log compression, full contrast stretch, etc.)
  - post_process_image(): Write your code to perform post-processing here. 
-  For this part of the assignment, You can use **inbuilt functions to compute the Fourier transform**.
- For example, **you are welcome to use fft and dft libraries that are available in numpy and opencv**
- This part of the assignment can be run using dip_hw3_part_3.py (Do Not modify this file)
- Usage: 

      python dip_hw3_part_3.py
  - Please make sure your code runs when you run the above command from prompt/terminal
  - Do not save any output in your code. Any output images or files will be saved to "output/" folder (dip_hw3_filter.py automatically does this)
  
-------------
**Note:**
We are **restricted from importing cv2, numpy, stats and other third party libraries,** 
with the only exception of math, importing math library is allowed (import math).

While you can import it for testing purposes, the final submission should not contain the following statements.
- import cv2
- import numpy
- import numpy as np
- import stats
- etc...

The essential functions for the assignment are available in dip module one can import using the following statement
```
import dip
from dip import *
```
The following functions are available

```commandline
from cv2 import namedWindow, imshow, waitKey, imwrite, imread, putText
from cv2 import FONT_HERSHEY_SIMPLEX, LINE_AA
from cv2 import ellipse, rectangle, circle

from numpy import zeros, ones, array, shape, arange
from numpy import random
from numpy import min, max
from numpy import uint8
from numpy import inf
from numpy.fft import fft2, fftshift, ifftshift, ifft2

import matplotlib
import matplotlib.pyplot as plt
```

*Assigments that contain any files that import these libraries will not be graded.* 
*Assigments that modify the dip.py file will not be graded.*

PS. Files not to be changed: requirements.txt and Jenkinsfile  
You are not allowed to change the overall code structure, and the main files:
- dip_hw3_part_1.py
- dip_hw3_part_2.py
- dip_hw3_part_3.py

Delete all your print-out statements unless it's required.



1. DFT                      - 15 Pts.
2. Linear Filtering         - 30 Pts.
2. FrequencyFiltering       - 30 Pts.

Total                       - 75 Pts.

---------------------
<sub><sup>License: Property of Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston.
This software is the property of the QIL, and should not be distributed, reproduced, or shared online, without the permission of the author
This software is intended to be used by students of the digital image processing course offered at the University of Houston.
The contents are not to be reproduced and shared with anyone without the permission of the author.
The contents are not to be posted on any online public hosting websites without the permission of the author.
The software is cloned and is available to the students for the duration of the course.
At the end of the semester, the GitHub organization is reset, and hence all the existing repositories are reset/deleted, to accommodate the next batch of students.</sub></sup>
