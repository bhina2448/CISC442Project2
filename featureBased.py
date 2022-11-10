#Feature Based analysis
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
def featureBased(left,right,method,searchRange,templateW,templateH):
    depth =np.zeros(left.shape, dtype=np.float32)
    row,col=left.shape
    width= (int)(row / templateW)*templateW
    height=(int)(col/templateH)*templateH
    cornersLeft= cv.goodFeaturesToTrack(left,100,0.1,10)
    cornersRight= cv.goodFeaturesToTrack(right,100,0.1,10)
    for corner in cornersLeft:
        x,y=corner.ravel()
        xstart=int(x-int(templateW/2))
        xend=int(x+int(templateW/2))
        ystart=int(y-int(templateH/2))
        yend=int(y+int(templateH/2))
        if xstart<0:
            n=abs(xstart)
            xend=xend+n
            xstart=0
        if xend> width-int(templateW/2)-1:
            val=xend -(width-int(templateW/2)-1)
            xstart=xstart-val
            xend=width-int(templateW/2)-1
        if ystart<0:
            n=abs(ystart)
            yend=yend+n
            ystart=0
        if yend> height-int(templateH/2)-1:
            val=yend -(height-int(templateH/2)-1)
            ystart=ystart-val
            yend=height-int(templateH/2)-1
        curr=left[xstart:xend, ystart:yend]
        disparity=getDisp(method,curr,y,x,cornersRight,right,templateW,templateH,searchRange)
        #update depth map values
        for i in range(xstart,xend):
            for j in range(ystart,yend):
                depth[i,j]=disparity

    depth=cv.normalize(depth,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    return depth

#returns the dispartiry using the given method
#searches for the template in the given image
def getDisp(method,template, templateypos,templatexpos,rightCorners, rightImg,templateW,templateH,searchRange):
    if method=="SAD":
        return SADDispCorner(template,templateypos,templatexpos,rightCorners,rightImg,templateW,templateH,searchRange)
    elif method=="SSD":
        return SSDDispCorner(template,templateypos,templatexpos,rightCorners,rightImg,templateW,templateH,searchRange)
    else:
        return NCCDispCorner(template,templateypos,templatexpos,rightCorners,rightImg,templateW,templateH,searchRange)

