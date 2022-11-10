from featureBased import *
from regionBased import *
import cv2 as cv
import numpy as np

left=cv.imread("venus0.png")
right=cv.imread("venus4.png")
left=cv.cvtColor(left, cv.COLOR_BGR2GRAY)
right=cv.cvtColor(right, cv.COLOR_BGR2GRAY)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)

method="NCC"
searchRange=200
templateW=9
templateH=9

disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("venus-NCC-RB-1.png", disparity)
print("photo 1 done")

disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("venus-NCC-FB-2.png", disparity)
print("photo 2 done")

left=cv.GaussianBlur(left,(5,5),0)
right=cv.GaussianBlur(right,(5,5),0)
method="SAD"

disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("venus-SAD-RB-3.png", disparity)
print("photo 3 done")

disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("venus-SAD-FB-4.png", disparity)
print("photo 4 done")

method="SSD"
disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("venus-SSD-RB-5.png", disparity)
print("photo 5 done")

disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("venus-SSD-FB-6.png", disparity)
print("photo 6 done")


left=cv.imread("tsukuba1.jpg")
right=cv.imread("tsukuba2.jpg")
left=cv.cvtColor(left, cv.COLOR_BGR2GRAY)
right=cv.cvtColor(right, cv.COLOR_BGR2GRAY)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)

method="NCC"
searchRange=255
templateW=5
templateH=5

disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("tsukuba-NCC-RB-7.png", disparity)
print("photo 7 done")

disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("tsukuba-NCC-FB-8.png", disparity)
print("photo 8 done")

left=cv.GaussianBlur(left,(5,5),0)
right=cv.GaussianBlur(right,(5,5),0)
method="SAD"

disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("tsukuba-SAD-RB-9.png", disparity)
print("photo 9 done")

disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("tsukuba-SAD-FB-10.png", disparity)
print("photo 10 done")

method="SSD"
disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("tsukuba-SSD-RB-11.png", disparity)
print("photo 11 done")

disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("tsukuba-SSD-FB-12.png", disparity)
print("photo 12 done")