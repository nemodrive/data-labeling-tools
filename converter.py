import numpy as np
import cv2
import os

if not os.path.exists("Output"):
    os.makedirs("Output")

cap = cv2.VideoCapture('driving.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
x = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
y = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print (x,y,fps)
out = cv2.VideoWriter('output.avi',fourcc, fps/5, (x,y))
nr = 0
nr2 = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret!=True:
        break
    if nr%5 ==0:
        out.write(frame)
        name = 'Output/out ' + str(nr2) + '.jpg'
        cv2.imwrite(name,frame)
        nr2 = nr2 + 1
    nr = nr + 1
    

print (nr)
# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
