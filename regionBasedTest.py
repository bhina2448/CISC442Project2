from regionBased import *
import cv2 as cv

l=cv.imread('venus0.png')
left=cv.cvtColor(l, cv.COLOR_BGR2GRAY)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
r=cv.imread('venus4.png')
right=cv.cvtColor(r, cv.COLOR_BGR2GRAY)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)
method="NCC"
searchRange=75
templateW=21
templateH=21

disparity=regionBased(left,right,method,searchRange,templateW,templateH)

cv.imwrite("disparity-RB-NCC-DOWNSIZED.png", disparity)
print("done")