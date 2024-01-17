[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LqtWd28I)
# Digital Image Processing 
Assignment #1

Due: Thu 09/28/23 11:59 PM

1. (20 pts.) Forward Rotation: Write code to perform forward rotation on an image.
    - Starter code available in directory Tranform/
    - Transform/geometric.py: Edit the function forward_rotate to implement this part.
    
2. (20 pts.) Reverse Rotation: Write code to perform reverse rotation on the input image.
    - Starter code available in directory Tranform/
    - Transform/geometric.py: Edit the function reverse_rotation to implement this part.
    
2. (35 pts.) Rotation with interpolation: Write code to rotate the input image, using nearest neighbor and bilinear interpolation.
    - Starter code available in directory Tranform/
    - Transform/geometric.py: Edit the function rotate to implement this part.
    - Transform/interpolation.py: Write code for linear and bilinear interpolation in there respective function definitions, you are welcome to write new functions and call them from these functions


  - The assignment can be run using dip_hw1_rotate.py (there is no need to edit this file)
  - Usage: `python dip_hw1_rotate.py -i image-name -t theta -m method`                   
       - image-name: name of the image
       - theta: angle in radians to rotate the image (eg. 0.5)
       - method: "nearest_neightbor" or "bilinear" 
  - Please make sure your code runs when you run the above command from prompt/Terminal
  - Any output images or files must be saved to "output/" folder

----------------------
One images is provided for testing: cameraman.jpg
  
Notes: 

1. Files not to be changed: requirements.txt, dip.py, and Jenkinsfile 

2. the code has to run using one of the following commands

 - Usage: `./dip_hw1_rotate.py -i image-name -t theta -m method`
 
   Example: `./dip_hw1_rotate.py -i cameraman.jpg -t 0.5 -m nearest_neighbor`

 - Usage: `python dip_hw1_rotate.py -i image-name -t theta -m method`
 
   Example: `python dip_hw1_rotate.py -i cameraman.jpg -t 0.5 -m bilinear`
  
3. Any output file or image should be written to output/ folder

4. The code has to run on jenkins CI/CD


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
from cv2 import namedWindow, imshow, waitKey, imwrite, imread
from cv2 import putText, LINE_AA, FONT_HERSHEY_SIMPLEX

from numpy import zeros, ones, array, shape, arange
from numpy import random
from numpy import min, max, sqrt, sum
from numpy import uint8
from numpy import inf
from numpy.fft import fft2
```

*Assigments that contain any files that import these libraries will not be graded.* 
*Assigments that modify the dip.py file will not be graded.*



Part| Name | Pts
--------------|-------------|----------
1|Forward rotation |- 20 Pts
2|Reverse rotation |- 20 Pts
3|Rotation interpolation |- 35 Pts
-|**Total**     | - **75 Pts**

-----------------------

<sub><sup>
License: Property of Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston. This software is property of the QIL, and should not be distributed, reproduced, or shared online, without the permission of the author This software is intended to be used by students of the digital image processing course offered at University of Houston. The contents are not to be reproduced and shared with anyone with out the permission of the author. The contents are not to be posted on any online public hosting websites without the permission of the author. The software is cloned and is available to the students for the duration of the course. At the end of the semester, the Github organization is reset and hence all the existing repositories are reset/deleted, to accommodate the next batch of students.
</sub></sup>

