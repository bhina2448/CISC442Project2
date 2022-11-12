from featureBased import *
from regionBased import *
from validCheck import *
import cv2 as cv
import numpy as np

left=cv.imread("venus0.png")
right=cv.imread("venus4.png")
left=cv.cvtColor(left, cv.COLOR_BGR2GRAY)
right=cv.cvtColor(right, cv.COLOR_BGR2GRAY)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)

method="SAD"
templateW=5
templateH=5
searchRange=50

#disparity=regionBased(left,right,method,searchRange,templateW,templateH)
#cv.imwrite("venusresult1.png", disparity)

method="SSD"
#disparity=regionBased(left,right,method,searchRange,templateW,templateH)
#cv.imwrite("venusresult2.png", disparity)

method="NCC"
#disparity=regionBased(left,right,method,searchRange,templateW,templateH)
#cv.imwrite("venusresult3.png", disparity)

left=cv.imread("tsukuba1.jpg")
right=cv.imread("tsukuba2.jpg")
left=cv.cvtColor(left, cv.COLOR_BGR2GRAY)
right=cv.cvtColor(right, cv.COLOR_BGR2GRAY)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)

method="SSD"
templateW=5
templateH=5
searchRange=50

#disparity=regionBased(left,right,method,searchRange,templateW,templateH)
#cv.imwrite("tsukubaresult1.png", disparity)

methos="SAD"
#disparity=regionBased(left,right,method,searchRange,templateW,templateH)
#cv.imwrite("tsukubaresult2.png", disparity)

method="SSD"
#disparity=featureBased(left,right,method,searchRange,templateW,templateH)
#cv.imwrite("tsukubaresult3.png", disparity)

method="SAD"
#disparity=featureBased(left,right,method,searchRange,templateW,templateH)
#cv.imwrite("tsukubaresult4.png", disparity)

left=cv.imread("sawtooth0.jpg")
right=cv.imread("sawtooth1.jpg")
left=cv.cvtColor(left, cv.COLOR_BGR2GRAY)
right=cv.cvtColor(right, cv.COLOR_BGR2GRAY)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)

method="SSD"
templateW=3
templateH=3
searchRange=50

disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("sawtoothresult1.png", disparity)

templateW=5
templateH=5

disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("sawtoothresult2.png", disparity)

templateW=9
templateH=9

disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("sawtoothresult3.png", disparity)
print("done sawtooh 3")

left=cv.imread("map0.jpg")
right=cv.imread("map1.jpg")
left=cv.cvtColor(left, cv.COLOR_BGR2GRAY)
right=cv.cvtColor(right, cv.COLOR_BGR2GRAY)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)

method="SAD"
templateW=5
templateH=5
searchRange=50

disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("mapresult1.png", disparity)
print("done map 1")

method="SSD"
disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("mapresult2.png", disparity)
print("done map 2")

method="NCC"
disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("mapresult3.png", disparity)
print("done map 3")

left=cv.imread("barn0.jpg")
right=cv.imread("barn1.jpg")
left=cv.cvtColor(left, cv.COLOR_BGR2GRAY)
right=cv.cvtColor(right, cv.COLOR_BGR2GRAY)
left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
right=cv.resize(right,(0,0),fx=0.5,fy=0.5)

method="SAD"
templateW=5
templateH=5
searchRange=50

disparity=featureBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("barnresult1.png", disparity)
print("done barn 1")

disparity=check(left,right,method,searchRange,templateW,templateH,"feature")
cv.imwrite("barnresult2.png", disparity)
print("done barn 2")

disparity=regionBased(left,right,method,searchRange,templateW,templateH)
cv.imwrite("barnresult3.png", disparity)
print("done barn 3")

disparity=check(left,right,method,searchRange,templateW,templateH,"region")
cv.imwrite("barnresult4.png", disparity)
print("done barn 4")