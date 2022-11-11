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
    #left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
    #right=cv.resize(right,(0,0),fx=0.5,fy=0.5)
    depth =np.zeros(left.shape, dtype=np.float32)
    row,col=left.shape
    cornersLeft=getCorners(left)
    edges=getEdges(left)
    features= np.append(cornersLeft,edges,axis=0)
    for corner in features:
        x,y=corner.ravel()
        xstart=int(x-int(templateW/2))
        xend=int(x+int(templateW/2))
        ystart=int(y-int(templateH/2))
        yend=int(y+int(templateH/2))
        if (xend<row)& (yend<col)&(xstart>0)&(ystart>0):
            curr=left[xstart:xend, ystart:yend]
            disparity=getDisp(curr,right,method,searchRange,x,y)
            #update depth map values
            depth[xstart,ystart]=disparity
            #for i in range(xstart,xend):
                #for j in range(ystart,yend):
                    #if(depth[i,j]==0):
                        #depth[i,j]=disparity
                    #else:
                        #dval=depth[i,j]
                        #avg=int((dval+disparity)/2)
                        #depth[i,j]=avg
    #depth=cv.normalize(depth,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    #depth=cv.resize(depth,(0,0),fx=2,fy=2)
    print("calling interpolate")
    depth=interpolate(depth)
    print("interpolate done")
    #depth=cv.medianBlur(depth,5)
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
    #image=cv.GaussianBlur(image,(5,5),0)
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
    #img=cv.GaussianBlur(image,(5,5),0)
    edges = cv.Canny(image,100,200)
    row,col=image.shape
    for x in range(0, row):
        for y in range(0,col):
            if edges[x,y]>50:
                edgesPos=np.append(edgesPos,np.array([[x,y]]),axis=0)
    return edgesPos

def paint(map):
    mask=np.zeros(map.shape)
    row,col=map.shape
    for x in range(0,row):
        for y in range(0,col):
            if map[x,y]==0:
                mask[x,y]=255
    mask=cv.normalize(mask,None, alpha=0,beta=255,norm_type=cv.NORM_MINMAX,dtype=cv.CV_8U)
    output=cv.inpaint(map,mask,3,cv.INPAINT_TELEA)
    return output

def interpolate(mapArr):
    output=np.zeros(mapArr.shape)
    row,col=mapArr.shape
    search=3
    found=np.empty((0,2),int)
    foundNum=0
    for x in range(0,row):
        for y in range(0,col):
            if mapArr[x,y]!=0:
                output[x,y]=mapArr[x,y]
            else:
                while(foundNum<1):
                    xstart=int(x-search)
                    xend=int(x+search)
                    ystart=int(y- search)
                    yend=int(y + search)
                    if xstart<0:
                        xstart=0
                    if xend> row-1:
                        xend=int(row-1)
                    if ystart<0:
                        ystart=0
                    if yend> col-1:
                        yend=int(col-1)
                    curr=mapArr[xstart:xend, ystart:yend]
                    crow,ccol=curr.shape
                    for i in range(0,crow):
                        for j in range(0,ccol):
                            if curr[i,j]!=0:
                                found=np.append(found,np.array([[i,j]]),axis=0)
                                foundNum=foundNum+1
                    if foundNum==0:
                        if search>500:
                            #check to avoid infitie loop
                            search=5
                            break
                        else:
                            search=search*3
                closestDist=200
                closestVal=0
                for pt in found:
                    i,j=pt.ravel()
                    xdist=(x-i)**2
                    ydist=(y-j)**2
                    dist=math.sqrt(xdist+ydist)
                    if(dist<closestDist):
                        closestDist=dist
                        closestVal=mapArr[i,j]
                    elif(dist==closestDist):
                        nVal=int(mapArr[i,j])
                        closestVal=int((closestVal+nVal)/2)
                output[x,y]=closestVal
                search=5
                found=np.empty((0,2),int)
                foundNum=0


    return output
        



