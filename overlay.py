from subprocess import check_output
import numpy as np
import cv2
from os import listdir
from os.path import isfile, join
import re
import os
from shutil import copyfile


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]



path = "Real_out"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]


onlyfiles = sorted(onlyfiles, key=natural_keys)

jpgs = []
masks = []
for i in onlyfiles:
    if "color" in i:
        masks.append(i)
    elif "jpg" in i:
        jpgs.append(i)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
img1 = cv2.imread(path + "/" + masks[0])
out = cv2.VideoWriter("overlay.avi",fourcc, 30, (img1.shape[1],img1.shape[0]))
for i in range(len(masks)):
        img1 = cv2.imread(path + "/" + masks[i])
        img2 = cv2.imread(path + "/" + jpgs[i])
        #img1[img1[:, :, 1:].all(axis=-1)] = 0
        #img2[img2[:, :, 1:].all(axis=-1)] = 0
        output = cv2.addWeighted(img1, 0.4, img2,1, 0)
        cv2.imshow('image',output)
        print(i)
        cv2.waitKey(0)
        out.write(output)

out.release()
