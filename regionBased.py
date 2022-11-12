#Region Based analysis
import numpy as np
import cv2 as cv
import math

def regionBased(left,right,method,searchRange,templateW,templateH):
    disp=0
    if method=="NCC":
        disp=regionNCC(left,right,searchRange,templateW,templateH)
    else:
        disp=blockMatch(left,right,method,searchRange,templateW,templateH)
    return fix(disp)

#left, right are the images
#method is either SAD, SSD, NCC
#searchRange is th emax distanct to search
#templateW and templateH is the width and heights of the template
def blockMatch(left,right,method,searchRange,templateW,templateH):
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
                if g<ghat or ghat<0:
                    ghat=g
                    dhat=d
            dispmap[x,y]=dhat
    dispmap=cv.normalize(dispmap,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    #dispmap=cv.GaussianBlur(dispmap,(0,0),3)
    return dispmap
def dissim(A,B,method):
    if method== "SAD":
        return abs(int(A)-int(B))
    else:
        return (int(A)-int(B))**2

#left, right are the images
#method is either SAD, SSD, NCC
#searchRange is th emax distanct to search
#templateW and templateH is the width and heights of the template
def regionNCC(left,right,searchRange,templateW,templateH):
    dispmap=np.zeros(left.shape,dtype=np.float32)
    width,height=left.shape
    for y in range (0,height-1-int(templateH/2)):
        for x in range (0,width-1-int(templateW/2)):
            ghat=0.0
            dhat=0
            for d in range(1,searchRange):
                g=0.0
                for j in range((1-int(templateH/2)),(1+int(templateH/2))):
                    for i in range((1-int(templateW/2)),(1+int(templateW/2))):
                        g=g+ncc(left[x+i,y+j],right[x+i-d,y+j])
                if g<ghat:
                    ghat=g
                    dhat=d
            dispmap[x,y]=dhat
    dispmap=cv.normalize(dispmap,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    return dispmap

def ncc(a,b):
    num=float(a)*float(b)
    den=float((a)**2)*float((b)**2)
    ncc=float(num)/ float(math.sqrt(den))
    return 1-ncc

def fix(dispmap):
    width,height=dispmap.shape
    for y in range (0,height-1):
        for x in range(0,width-1):
            val=dispmap[x,y]
            if val==0:
                dispmap[x,y]=0
            elif val<20:
                dispmap[x,y]=50
            elif val<=51:
                dispmap[x,y]=50
            elif val<=102:
                dispmap[x,y]=100
            elif val<=153:
                dispmap[x,y]=100
            elif val<=204:
                dispmap[x,y]=200
            elif val<255:
                dispmap[x,y]=200
            else:
                dispmap[x,y]=255
    return dispmap