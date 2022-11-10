#Feature Based analysis
import numpy as np
import cv2 as cv
from scipy.interpolate import interp2d
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
    #cornersLeft= cv.goodFeaturesToTrack(left,2000,0.04,1)
    cornersLeft=getCorners(left)
    edges=getEdges(left)
    features= np.append(cornersLeft,edges,axis=0)
    for corner in features:
        x,y=corner.ravel()
        xstart=int(x)
        xend=int(x+templateW)
        ystart=int(y)
        yend=int(y+templateH)
        if (xend<row)& (yend<col):
            curr=left[xstart:xend, ystart:yend]
            disparity=getDisp(curr,right,method,searchRange,xstart,ystart)
            #update depth map values
            #depth[xstart,ystart]=disparity
            for i in range(xstart,xend):
                for j in range(ystart,yend):
                    if(disparity>depth[i,j]):
                        depth[i,j]=disparity
    depth=interpolate(depth)
    depth=cv.medianBlur(depth,5)
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

#returns an array of all of the positions of corners in a greyscal image
def getCorners(image):
    corners=np.empty((0,2),int)
    image=cv.blur(image,(5,5))
    img=np.float32(image)
    dst=cv.cornerHarris(img,5,3,0.04)
    dst=cv.dilate(dst,None)
    trsh=0.01*dst.max()
    for x in range(0,dst.shape[0]):
        for y in range(0,dst.shape[1]):
            if(dst[x,y]>trsh):
                corners=np.append(corners,np.array([[x,y]]),axis=0)
    return corners

def getEdges(image):
    edgesPos=np.empty((0,2),int)
    img=cv.GaussianBlur(image,(5,5),0)
    edges = cv.Canny(img,100,200)
    row,col=image.shape
    for x in range(0, row):
        for y in range(0,col):
            if edges[x,y]>50:
                edgesPos=np.append(edgesPos,np.array([[x,y]]),axis=0)
    return edgesPos

def interpolate(map):
    mask=np.zeros(map.shape)
    row,col=map.shape
    for x in range(0,row):
        for y in range(0,col):
            if map[x,y]==0:
                mask[x,y]=255
    mask=cv.normalize(mask,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    output=cv.inpaint(map,mask,3,cv.INPAINT_TELEA)
    return output
        



