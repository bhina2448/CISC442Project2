#Normalized Cross-correlation
import numpy as np
import math

#Gets the disparity using NCC
#searching for template in image
#xpos,ypos is templates position in original left side image
def NCCDisp(template, image, searchRange, xpos,ypos):
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
    nccVal=NCC(template,curr)
    for x in range(minx,maxx):
        curr=image[x:x+trow,ypos-int(tcol/2):ypos+int(tcol/2)+1]
        val=NCC(template,curr)
        if(val==nccVal):
            d=abs(xpos-(x+int(trow/2)))
            if(d<disp):
                disp=d
        elif(val<nccVal):
            nccVal=val
            disp=abs(xpos-(x+int(trow/2)))
    return disp


#computes NCC for arrays template and section (must be of same size)
def NCC(template, section):
    row,col= template.shape
    mult=0
    I1=0
    I2=0
    for x in range(0,row):
        for y in range(0,col):
            mult=mult+(int(template[x,y])*int(section[x,y]))
            I1=I1+int((template[x,y])**2)
            I2=I2+int((section[x,y])**2)
    ncc=mult/ math.sqrt(I1*I2)
    return 1-ncc