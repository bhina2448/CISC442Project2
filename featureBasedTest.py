from featureBased import *
import cv2 as cv
import numpy as np

l=cv.imread('tsukuba1.jpg')
left=cv.cvtColor(l, cv.COLOR_BGR2GRAY)
#left=cv.GaussianBlur(left,(9,9),0)
#left=cv.GaussianBlur(left,(5,5),0)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
#left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
r=cv.imread('tsukuba3.jpg')
right=cv.cvtColor(r, cv.COLOR_BGR2GRAY)
#right=cv.GaussianBlur(right,(9,9),0)
#right=cv.GaussianBlur(right,(5,5),0)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)
#right=cv.resize(right,(0,0),fx=0.5,fy=0.5)
method="SAD"
searchRange=64
templateW=5
templateH=5

disparity=featureBased(left,right,method,searchRange,templateW,templateH)
#disp=cv.GaussianBlur(disparity,(5,5),0)

cv.imwrite("tsukuba-FD-SAD-TEST10.png", disparity)
print("done")

