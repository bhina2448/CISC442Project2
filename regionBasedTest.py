from regionBased import *
import cv2 as cv

l=cv.imread('tsukuba1.jpg')
left=cv.cvtColor(l, cv.COLOR_BGR2GRAY)
#left=cv.medianBlur(left,5)
#left=cv.GaussianBlur(left,(5,5),0)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
#left=cv.resize(left,(0,0),fx=0.5,fy=0.5)

r=cv.imread('tsukuba3.jpg')
right=cv.cvtColor(r, cv.COLOR_BGR2GRAY)
#right=cv.medianBlur(right,5)
#right=cv.GaussianBlur(right,(5,5),0)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)
#right=cv.resize(right,(0,0),fx=0.5,fy=0.5)

method="SSD"
searchRange=50
templateW=5
templateH=5

disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("tsukuba-RB-SSD-5vals.png", disparity)
print("done")