#Region Based analysis
import numpy as np
import cv2 as cv
#left- left image
#right- right image
#method- either SAD, SSD, NCC
#searchRange- size of searching area
#templateW- width of the template
#templateH- height of the template
def regionBased(left,right,method,searchRange,templateW,templateH):
    depth =np.zeros(left.shape, dtype=np.float32)
    width= (int)(left.width / templateW)*templateW
    height=(int)(left.height/templateH)*templateH
    for x in range(0,(width-templateW-1)):
        for y in range(0,(height-templateH-1)):
            curr=left[x:x+templateW, y:y+templateH]
            disparity=getDisp(curr,right,method,searchRange,x,y)
            depth[x,y]=disparity
    depth=cv.normalize(depth,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    return depth

#returns the dispartiry using the given method
#searches for the template in the given image
def getDisp(template, image, method, searchRange, x,y):
    if method=="SAD":
        #use SAD
    else if method=="SSD":
        #use SSD
    else:
        #use NCC

