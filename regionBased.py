#Region Based analysis
import numpy as np
import cv2 as cv
from SAD import *
from SSD import *
from NCC import *

#left, right are the images
#method is either SAD, SSD, NCC
#searchRange is th emax distanct to search
#templateW and templateH is the width and heights of the template
def blockmatch(left,right,method,searchRange,templateW,templateH):
    dispmap=np.zeros(left.shape,dtype=np.float32)
    width,height=left.shape
    for y in range (0,height-1-int(templateH/2)):
        for x in range (0,width-1-int(templateW/2)):
            ghat=-1
            dhat=0
            for d in range(1,searchRange):
                g=0
                for j in range((1-int(templateH/2)),(1+int(templateH/2))):
                    for i in range((1-int(templateW/2)),(1+int(templateW/2))):
                        g=g+dissim(left[x+i,y+j],right[x+i-d,y+j],method)
                if g< ghat or ghat<0:
                    ghat=g
                    dhat=d
            dispmap[x,y]=dhat
    dispmap=cv.normalize(dispmap,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    return dispmap
def dissim(A,B,method):
    if method== "SAD":
        return abs(int(A)-int(B))
    elif method=="SSD":
        return (int(A)-int(B))**2
    else:
        num=float(A)*float(B)
        den=(float(A)**2)* (float(B)**2)
        return num/ math.sqrt(den)
