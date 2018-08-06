from subprocess import check_output
import numpy as np
import cv2
from os import listdir
from os.path import isfile, join
import re
import os
from shutil import copyfile


if not os.path.exists("Color_out"):
    os.makedirs("Color_out")
if not os.path.exists("Mask_out"):
    os.makedirs("Mask_out")
if not os.path.exists("Watershed_out"):
    os.makedirs("Watershed_out")
if not os.path.exists("Real_out"):
    os.makedirs("Real_out")
    
def move_files():
        
        path = "Output"
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

        for i in onlyfiles:
                if "color_mask" in i:
                    string = path + "/" + i;
                    dest =  "Color_out" + "/" +i;
                    copyfile(string, dest);
                elif "watershed_mask" in i:
                    string = path + "/" + i;
                    dest =  "Watershed_out" + "/" +i;
                    copyfile(string, dest);
                elif "mask" in i:
                    string = path + "/" + i;
                    dest =  "Mask_out" + "/" +i;
                    copyfile(string, dest);

def reconstruct():
    
    def put_video(path,out_name):
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        print (onlyfiles)
        key=lambda word: [alphabet.index(c) for c in word]

        onlyfiles = sorted(onlyfiles, key=natural_keys)

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(out_name,fourcc, 5.8, (1280,720))

        for i in onlyfiles:
            img = cv2.imread(os.path.join(path, i))
            print(i)
            print (img)
            out.write(img)


        out.release()

    put_video("Color_out","color_output.avi")
    put_video("Mask_out", "mask_output.avi")
    put_video("Watershed_out", "watershed_output.avi")
    
def reconverter():
    
    def put_files(video, mask,ext):
        cap = cv2.VideoCapture(video)

        nr = 0
        nr2 = 0
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret!=True:
                break
            name = 'Real_out/out ' + str(nr2) + mask + "." + ext
            cv2.imwrite(name,frame)
            nr2 = nr2 + 1

        # When everything done, release the capture
        cap.release()

    put_files("driving.mp4", "", "jpg")
    put_files("out_color.mp4","_color_mask","png")
    put_files("out_watershed.mp4","_watershed_mask","png")
    put_files("out_mask.mp4", "_mask","png")

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


def duplicate():
    onlyfiles = [f for f in listdir("Mask_out") if isfile(join("Mask_out", f))]
    onlyfiles = sorted(onlyfiles, key=natural_keys)

    nr = 0
    for i in onlyfiles:
        img = cv2.imread(os.path.join("Mask_out", i))
        for j in range(6):
            name = "Real_out/out " + str(nr) + "_mask.png"
            print (name)
            cv2.imwrite(name,img)
            nr = nr+1



move_files()
reconstruct()
check_output("call.bat")
reconverter()
duplicate()


print ("done")
