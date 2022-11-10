from featureBased import *
import cv2 as cv

l=cv.imread('sawtooth0.jpg')
left=cv.cvtColor(l, cv.COLOR_BGR2GRAY)
#left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
#left=cv.resize(left,(0,0),fx=0.5,fy=0.5)
r=cv.imread('sawtooth6.jpg')
right=cv.cvtColor(r, cv.COLOR_BGR2GRAY)
#right=cv.resize(right,(0,0),fx=0.5,fy=0.5)
#right=cv.resize(right,(0,0),fx=0.5,fy=0.5)
method="SAD"
searchRange=100
templateW=5
templateH=5

disparity=featureBased(left,right,method,searchRange,templateW,templateH)

cv.imwrite("sawtooth-FB-SAD.png", disparity)
print("done")