# data labeling tools
video tools:
- VitBat - doesn't load any video, offers only rectangle and point as bounding boxes
- Viper - old and doesn't even start
- CVAT and Vatic - good for object detection, simple interface , work for any video. 
	         - CVAT is the improved version of Vatic. Simple interface, web based
		 - launch with a simple docker-compose up -d command, go to localhost:8080
		 - you should also have a username and password (on hal - nemodrive / nemodrive)
		 - also support activity type for detected objects
		 - output: an XML file with all the annotations
- LabelMe Video - would be the best option, includes polygond bounding boxes, but it is discontinued
 		  and don't support video upload

Image tools for segmentation/ detection:
 - LabelMe - even if you can make some custom egmentation, the output will return only a rectangle
 - LabelBox - you can make polygon bounding boxes
 - PixelWise - only segmentation, best tool for segmentation as far as I found, you only draw some points and it  makes a mask with the result
             - output - image mask, so you have to parse the pixels manually for interpolation purposes

Semantic segmentation project:
https://github.com/asimonov/CarND3-P2-FCN-Semantic-Segmentation - Makes a good segmentation. Hard to train, but good results.

# Object annotation

Clone the repo from CVAT and do  the steps mentioned in their readme to start the program with docker. You can annotate directly on the video and save the results
as coordinates for the detected objects.

# Semantic segmentation:
We will use PixelWise and the scripts provided here. You must download PixelWise for windows and butterflow for windows.
Change the name of the video in converter.py from "driving.mp4" to your video, run converer.py then start 
drawing the segmentation in PixelWise for the Output/ folder that will be created.  The segmentation will be done only for 1/5 frames in the video.Then you have to run 
reconverter.py, and it will be created a new folder named Real_out, in which you can further adjust the interpolated frames. Finally, with overlay.py you can see
the segmentation result.