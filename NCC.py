#Normalized Cross-correlation
import numpy as np
import math

#Gets the disparity using NCC
#searching for template in image
#xpos,ypos is templates position in original left side image
def NCCDisp(template, image, searchRange, xpos,ypos):
    trow,tcol= template.shape
    irow,icol=image.shape
    curr=image[xpos:xpos+trow, ypos:ypos+tcol]
    disp=NCC(template,curr)
    minx=xpos-searchRange
    maxx=xpos+searchRange
    if(minx<0):
        minx=0
    if(maxx>= irow-trow):
        maxx= irow-trow -1
    for x in range(minx,maxx):
        curr=image[x:x+trow,ypos:ypos+tcol]
        val=NCC(template,curr)
        if(val<disp):
            disp=val
    return disp


#computes NCC for arrays template and section (must be of same size)
def NCC(template, section):
    row,col,dim= template.shape
    mult=0
    I1=0
    I2=0
    for x in range(0,row):
        for y in range(0,col):
            mult=mult+(int(template[x,y])*int(section[x,y]))
            I1=I1+int((template[x,y])**2)
            I2=I2+int((section[x,y])**2)
    ncc=int(mult/ math.sqrt(I1*I2))
    return ncc