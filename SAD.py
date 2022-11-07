#Sum of Absolute Differences
import numpy as np

#Gets the disparity using SAD
#searching for template in image
#xpos,ypos is templates position in original left side image
def SADDisp(template, image, searchRange, xpos,ypos):
    curr=image[xpos:xpos+template.width, ypos:ypos+template.height]
    disp=SAD(template,curr)
    minx=xpos-searchRange
    maxx=xpos+searchRange
    if(minx<0):
        minx=0
    if(maxx>= image.width-template.width):
        maxx= image.width-template.width -1
    for x in range(minx,maxx):
        curr=image[x:x+template.width,ypos:ypos+template.height]
        val=SAD(template,curr)
        if(val<disp):
            disp=val
    return disp


#computes SAD for arrays template and section (must be of same size)
def SAD(template, section):
    sum=0
    for x in range(0,template.width):
        for y in range(0,template.height):
            val=abs(template[x,y]-section[x,y])
            sum=sum+val
    return sum