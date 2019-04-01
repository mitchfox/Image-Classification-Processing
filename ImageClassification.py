import cv2
import numpy as np
import os
import time
import shutil

#  Image Sorter determined by Face, Colours, etc...
# 1. Face Detection
# 2. Sort Images
# 3. Sort based on Landscape (Dominant Colours / Oceans / Forests)


# Cascade Libraries
face_cascade = cv2.CascadeClassifier(
    '/usr/local/Cellar/opencv/4.0.1/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/4.0.1/share/opencv4/haarcascades/haarcascade_eye.xml')


# Filter through all Images in selected folder

# Change path to use different directories - '/Users/ect/ect...'
input_path = '/Users/Foxy/Desktop/photos'
output_path = '/Users/Foxy/Desktop/sorted'

hasFace = False

for filename in os.listdir(input_path):

    print('Scanning ' + filename)
    if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".png") or filename.endswith(".PNG"):
        target_image = cv2.imread((os.path.join(input_path, filename)))
        gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

        # Finding Faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            target_image = cv2.rectangle(target_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = target_image[y:y + h, x:x + w]

            # Face Bool set to true
            hasFace = True

            # Finding Eyes
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            if hasFace:
                print('Face Found within Image')

                # Show User Image of the Face Detection
                cv2.imshow('filename', target_image)
                # Wait for Key Press
                cv2.waitKey()
                cv2.destroyWindow('target_image')

                # Move Images to new directory
                shutil.move(input_path + '/' + filename, output_path)
                print('File Moved to New Directory')

            else:
                print('This Image has no Face. It will not be moved')
                cv2.imshow('filename' + 'NO FACE', target_image)
                cv2.waitKey()
                cv2.destroyWindow('target_image')


    else:
        print('This file is not supported | Please convert files to .jpg or .png')

print('All Images Scanned.')



