#Sum of squared differences
import numpy as np

#Gets the disparity using SSD
#searching for template in image
#xpos,ypos is templates position in original left side image
def SSDDisp(template, image, searchRange, xpos,ypos):
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
    ssdVal=SSD(template,curr)
    for x in range(minx,maxx):
        curr=image[x:x+trow,ypos-int(tcol/2):ypos+int(tcol/2)+1]
        val=SSD(template,curr)
        if(val==ssdVal):
            d=abs(xpos-(x+int(trow/2)))
            if(d<disp):
                disp=d
        elif(val<ssdVal):
            ssdVal=val
            disp=abs(xpos-(x+int(trow/2)))
    return disp


#computes SSD for arrays template and section (must be of same size)
def SSD(template, section):
    row,col= template.shape
    sum=0
    for x in range(0,row):
        for y in range(0,col):
            val=(int(template[x,y])-int(section[x,y]))**2
            sum=sum+val
    return sum