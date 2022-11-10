#Region Based analysis
import numpy as np
import cv2 as cv
from SAD import *
from SSD import *
from NCC import *
#left- left image
#right- right image
#method- either SAD, SSD, NCC
#searchRange- size of searching area
#templateW- width of the template
#templateH- height of the template
def regionBased(left,right,method,searchRange,templateW,templateH):
    depth =np.zeros(left.shape, dtype=np.float32)
    row,col=left.shape
    width= (int)(row / templateW)*templateW
    height=(int)(col/templateH)*templateH
    for x in range(0,(width-1)):
        for y in range(0,(height-1)):
            curr=left[x:x+templateW, y:y+templateH]
            disparity=getDisp(curr,right,method,searchRange,x,y)
            depth[x,y]=disparity
    depth=avgNeighborhood(depth,templateW,templateH,height,width)
    depth=cv.normalize(depth,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    return depth

#returns the dispartiry using the given method
#searches for the template in the given image
def getDisp(template, image, method, searchRange, x,y):
    if method=="SAD":
        return SADDisp(template,image,searchRange,x,y)
    elif method=="SSD":
        return SSDDisp(template,image,searchRange,x,y)
    else:
        return NCCDisp(template,image,searchRange,x,y)

def avgNeighborhood(depth, templateW,templateH,height, width):
    x=0
    y=0
    while(x<width-templateW-1):
        while(y< height-templateH-1):
            curr=depth[x:x+templateW, y:y+templateH]
            avg=np.average(curr)
            for i in range(x, x+templateW):
                for j in range(y,y+templateH):
                    depth[i,j]=avg
            y=y+templateH
        x=x+templateW
    return depth

