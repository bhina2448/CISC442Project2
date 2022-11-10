#Sum of Absolute Differences
import numpy as np

#Gets the disparity using SAD
#searching for template in image
#xpos,ypos is templates position in original left side image
def SADDisp(template, image, searchRange, xpos,ypos):
    trow,tcol= template.shape
    irow,icol=image.shape
    curr=image[xpos:xpos+trow, ypos:ypos+tcol]
    sadval=SAD(template,curr)
    disp=0
    minx=xpos-searchRange
    maxx=xpos+searchRange
    if(minx<0):
        minx=0
    if(maxx>= irow-trow):
        maxx= irow-trow -1
    for x in range(minx,maxx):
        curr=image[x:x+trow,ypos:ypos+tcol]
        val=SAD(template,curr)
        if(val<sadval):
            sadval=val
            disp=abs(xpos-x)
    return disp


#computes SAD for arrays template and section (must be of same size)
def SAD(template, section):
    sum=0
    row,col=template.shape
    for x in range(0,row):
        for y in range(0,col):
            val=abs(int(template[x,y])-int(section[x,y]))
            sum=sum+val
    return sum