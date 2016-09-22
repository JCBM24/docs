#!/usr/bin/env python3

import subprocess
import time
import cv2

DEVICE = 1
EXPOSURE = 10

# set exposure
dev = "video{}".format(DEVICE)
subprocess.run(["uvcdynctrl", "-d", dev, "-s", "Exposure, Auto", "1"])
subprocess.run(["uvcdynctrl", "-d", dev, "-s", "Exposure (Absolute)", str(EXPOSURE)])

# device 0 is the first camera found
camera = cv2.VideoCapture(DEVICE)

while True:
    # capture one frame
    retval, frame = camera.read()

    if not retval:
        print('No frame grabbed, is camera disconnected?')
        break

    # manipulate the frame
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_lower = (157 // 2 - 10, 100, 100)
    hsv_upper = (157 // 2 + 10, 255, 255)
    inrange_mask = cv2.inRange(hsv_frame, hsv_lower, hsv_upper)

    cv2.imshow('Processed', inrange_mask)
    time.sleep(0.02)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
