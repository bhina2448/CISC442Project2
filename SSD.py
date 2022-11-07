#Sum of squared differences
import numpy as np

#Gets the disparity using SSD
#searching for template in image
#xpos,ypos is templates position in original left side image
def SSDDisp(template, image, searchRange, xpos,ypos):
    curr=image[xpos:xpos+template.width, ypos:ypos+template.height]
    disp=SSD(template,curr)
    minx=xpos-searchRange
    maxx=xpos+searchRange
    if(minx<0):
        minx=0
    if(maxx>= image.width-template.width):
        maxx= image.width-template.width -1
    for x in range(minx,maxx):
        curr=image[x:x+template.width,ypos:ypos+template.height]
        val=SSD(template,curr)
        if(val<disp):
            disp=val
    return disp


#computes SSD for arrays template and section (must be of same size)
def SSD(template, section):
    sum=0
    for x in range(0,template.width):
        for y in range(0,template.height):
            val=(template[x,y]-section[x,y])**2
            sum=sum+val
    return sum