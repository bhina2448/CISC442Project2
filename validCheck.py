from regionBased import *
from featureBased import *

def check(left,right,method,searchRange,templateW,templateH,search):
    if search=="region":
        leftdisp=regionBased(left,right,method,searchRange,templateW,templateH)
        rightdisp=regionBased(right,left,method,searchRange,templateW,templateH)
    else:
        leftdisp=featureBased(left,right,method,searchRange,templateW,templateH)
        rightdisp=featureBased(right,left,method,searchRange,templateW,templateH)
    width,height=leftdisp.shape
    for y in range(0,height-1):
        for x in range(0,width-1):
            leftval=leftdisp[x,y]
            rightval=rightdisp[x,y]
            if abs(leftval-rightval)>=20:
                leftdisp[x,y]=0
                rightdisp[x,y]=0
    if method== "region":
        return avgNeighborhood(left,templateW,templateH,height, width)
    else:
        return leftdisp

def avgNeighborhood(depth, templateW,templateH,height, width):
    x=0
    y=0
    while(x<width-templateW-1):
        while(y< height-templateH-1):
            if depth[x,y]==0:
                curr=depth[x:x+templateW, y:y+templateH]
                avg=np.average(curr)
                depth[x,y]=avg
            y=y+templateH
            x=x+templateW
    return depth