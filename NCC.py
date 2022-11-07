#Normalized Cross-correlation
import numpy as np
import math

#Gets the disparity using NCC
#searching for template in image
#xpos,ypos is templates position in original left side image
def NCCDisp(template, image, searchRange, xpos,ypos):
    curr=image[xpos:xpos+template.width, ypos:ypos+template.height]
    disp=NCC(template,curr)
    minx=xpos-searchRange
    maxx=xpos+searchRange
    if(minx<0):
        minx=0
    if(maxx>= image.width-template.width):
        maxx= image.width-template.width -1
    for x in range(minx,maxx):
        curr=image[x:x+template.width,ypos:ypos+template.height]
        val=NCC(template,curr)
        if(val<disp):
            disp=val
    return disp


#computes NCC for arrays template and section (must be of same size)
def NCC(template, section):
    mult=0
    I1=0
    I2=0
    for x in range(0,template.width):
        for y in range(0,template.height):
            mult=mult+(template[x,y]*section[x,y])
            I1=I1+(template[x,y])**2
            I2=I2+(section[x,y])**2
    ncc=mult/ math.sqrt(I1*I2)
    return ncc