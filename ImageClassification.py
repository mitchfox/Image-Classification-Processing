import cv2
import numpy as np
import os

""" Image Sorter determined by Face, Colours, etc...
1. Face Detection
2. Sort Images
3. Sort based on Landscape (Dominant Colours / Oceans / Forrests)
"""

# Face Detection Bool
hasFace = False

# Filter through all Images in selected folder

# Cascades
face_cascade = cv2.CascadeClassifier(
    '/usr/local/Cellar/opencv/4.0.1/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/4.0.1/share/opencv4/haarcascades/haarcascade_eye.xml')

# Future add user allowable input for custom directory
for filename in os.listdir('/Users/Foxy/Desktop/photos'):

    print('Testing Images...')
    if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".png") or filename.endswith(".PNG"):
        print(filename)
        target_image = cv2.imread((os.path.join('/Users/Foxy/Desktop/photos', filename)))
        gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            target_image = cv2.rectangle(target_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = target_image[y:y + h, x:x + w]

            # Finding Eyes
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow('targetImage', target_image)


    else:
        print('This file is not supported')

    # Wait for command

    cv2.waitKey(0)
    cv2.destroyAllWindows()




