from subprocess import check_output
import numpy as np
import cv2
from os import listdir
from os.path import isfile, join
import re
import os
from shutil import copyfile
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture("camera_3.avi")
cap2 = cv2.VideoCapture("camera_0.avi")
x = time.time()
while(True):
        
    ret, frame = cap.read()
    if ret!=True:
        break
    ret2, frame2 = cap2.read()
    if ret2!=True:
        break
    frame_new=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2_new=cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    crop_img = frame_new[0:620,0:]
    crop_img2 = frame2_new[0:720,:]
    cv2.imwrite("img1.jpg",frame)
    cv2.imwrite("img2.jpg",frame2)
    cv2.imwrite("img1cr.jpg",crop_img)
    cv2.imwrite("img2cr.jpg",crop_img2)

    imgL = frame_new
    imgR = frame2_new
   # stereo = cv2.StereoSGBM_create(numDisparities=16, blockSize=15)
    #disparity = stereo.compute(frame_new,frame2_new)
   # print (disparity)
   # plt.imshow(disparity, 'plasma')
   # plt.show()
   # plt.imwrite("img.jpg",disparity)
    #cv2.waitKey(0)
    window_size = 3 
    left_matcher = cv2.StereoSGBM_create(
    minDisparity=0,
    numDisparities=160,             # max_disp has to be dividable by 16 f. E. HH 192, 256
    blockSize=5,
    P1=8 * 3 * window_size ** 2,    # wsize default 3; 5; 7 for SGBM reduced size image; 15 for SGBM full size image (1300px and above); 5 Works nicely
    P2=32 * 3 * window_size ** 2,
    disp12MaxDiff=1,
    uniquenessRatio=15,
    speckleWindowSize=0,
    speckleRange=2,
    preFilterCap=63,
    mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
)
    right_matcher = cv2.ximgproc.createRightMatcher(left_matcher)
    # FILTER Parameters
    lmbda = 80000
    sigma = 1.2
    visual_multiplier = 1.0
     
    wls_filter = cv2.ximgproc.createDisparityWLSFilter(matcher_left=left_matcher)
    wls_filter.setLambda(lmbda)
    wls_filter.setSigmaColor(sigma)

   # print('computing disparity...')
    displ = left_matcher.compute(imgL, imgR)  # .astype(np.float32)/16
    dispr = right_matcher.compute(imgR, imgL)  # .astype(np.float32)/16
    displ = np.int16(displ)
    dispr = np.int16(dispr)
    filteredImg = wls_filter.filter(displ, imgL, None, dispr)
    filteredImg = cv2.normalize(src=filteredImg, dst=filteredImg, beta=0, alpha=255, norm_type=cv2.NORM_MINMAX);
    filteredImg = np.uint8(filteredImg)
    cv2.imshow('Disparity Map', filteredImg)
    cv2.waitKey()
    print ( time.time()-x)

