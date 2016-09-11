#!/usr/bin/env python3

import time
import cv2

# device 0 is the first camera found
camera = cv2.VideoCapture(0)

while True:
    # capture one frame
    retval, frame = camera.read()

    if not retval:
        print('No frame grabbed, is camera disconnected?')
        break

    # manipulate the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (15, 15), 5)
    _, thresholded = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

    # display the frame
    cv2.imshow('Processed', thresholded)
    time.sleep(0.02)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
