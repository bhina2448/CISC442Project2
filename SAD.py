#Sum of Absolute Differences
import numpy as np
import cv2 as cv

#Gets the disparity using SAD
#searching for template in image
#xpos,ypos is templates position in original left side image
def SADDisp(template, image, searchRange, xpos,ypos):
    trow,tcol= template.shape
    irow,icol=image.shape
    disp=0
    minx=xpos-searchRange
    maxx=xpos+searchRange
    if(minx<0):
        minx=0
    if(maxx>= irow-trow):
        maxx= irow-trow -1
    curr=image[minx:minx+trow, ypos-int(tcol/2):ypos+int(tcol/2)+1]
    ssdVal=SAD(template,curr)
    for x in range(minx,maxx):
        curr=image[x:x+trow,ypos-int(tcol/2):ypos+int(tcol/2)+1]
        val=SAD(template,curr)
        if(val==ssdVal):
            d=abs(xpos-(x+int(trow/2)))
            if(d<disp):
                disp=d
        elif(val<ssdVal):
            ssdVal=val
            disp=abs(xpos-(x+int(trow/2)))
    return disp


def SADold(left,right,startx,endx,starty,endy,d):
    sum=0
    for x in range(startx,endx):
        for y in range(starty,endy):
            val=abs(int(left[x+d,y])-int(right[x,y]))
            sum=sum+val
    return sum

#computes SAD for arrays template and section (must be of same size)
def SAD(template, section,):
    sum=0
    row,col=template.shape
    for x in range(0,row):
        for y in range(0,col):
            val=abs(int(template[x,y])-int(section[x,y]))
            sum=sum+val
    return sum