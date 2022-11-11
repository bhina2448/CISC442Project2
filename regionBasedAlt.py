#Region Based analysis didnt have the heart to get rid of it
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
def regionBasedALT(left,right,method,searchRange,templateW,templateH):
    depth =np.zeros(left.shape, dtype=np.float32)
    row,col=left.shape
    width= int(row-(templateW-1))
    height=int(col-(templateH-1))
    for x in range(0,width):
        for y in range(0,height):
            curr=left[x:x+templateW, y:y+templateH]
            xpos=x+int(templateW/2)
            ypos=y+int(templateH/2)
            disparity=getDisp(method,curr,right,left,searchRange,xpos,ypos)
            depth[xpos,ypos]=disparity
    #depth=avgNeighborhood(depth,templateW,templateH,height,width)
    depth=cv.normalize(depth,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    return depth

#returns the dispartiry using the given method
#searches for the template in the given image
def getDisp(method,template, right,left, searchRange, xpos,ypos):
    if method=="SAD":
        return SADDisp(template, right,left, searchRange, xpos,ypos)
    elif method=="SSD":
        return SSDDisp(template,right,searchRange,xpos,ypos)
    else:
        return NCCDisp(template,right,searchRange,xpos,ypos)

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