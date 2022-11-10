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

#gets the disparity using corner detection and NCC 
#template is the section of the left image to search for
#templateypos and templatexpos is the x,y position of the template in the original right image
#right corners is all of the corners detected in the right image
#rightImg is the original right image
#templateW and templateH is the height and weight of the template
#searchRange is the max range that will be searched
def NCCDispCorner(template, templateypos,templatexpos,rightCorners, rightImg,templateW,templateH,searchRange):
    row,col=rightImg.shape
    width= (int)(row / templateW)*templateW
    height=(int)(col/templateH)*templateH
    disp=255
    for corner in rightCorners:
        x,y=corner.ravel()
        if(y==templateypos)& (x<=templatexpos+searchRange):
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
            curr=rightImg[xstart:xend, ystart:yend]
            val=NCC(template,curr)
            if(val<disp):
                disp=val
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
    ncc=int(mult/ math.sqrt(I1*I2))
    return ncc