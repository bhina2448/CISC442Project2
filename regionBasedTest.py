from regionBased import *
import cv2 as cv

l=cv.imread('venus0.png')
left=cv.cvtColor(l, cv.COLOR_BGR2GRAY)
r=cv.imread('venus4.png')
right=cv.cvtColor(r, cv.COLOR_BGR2GRAY)
method="SSD"
searchRange=50
templateW=5
templateH=5

disparity=regionBased(left,right,method,searchRange,templateW,templateH)

cv.imwrite("disparity-RB-SSD.png", disparity)
print("done")