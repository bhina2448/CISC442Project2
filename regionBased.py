#Region Based analysis
import numpy as np
import cv2 as cv
#left- left image
#right- right image
#method- either SAD, SSD, NCC
#searchRange- size of searching area
#templateX- x value for size of the template
#templateY- y value for size of the template
#disparity- disparity (horizontal motion)
def regionBased(left,right,method,searchRange,templateX,templatY, disparity):
    depth =np.zeros(left.shape, dtype=np.float32)
    