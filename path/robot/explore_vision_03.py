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
    _, contours, _ = cv2.findContours(inrange_mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    max_area_index = 0
    current_index = 0
    if len(contours) == 0:
        continue
    for c in contours:
        area = cv2.contourArea(c)
        if area > max_area:
            max_area = area
            max_area_index = current_index
        current_index = current_index + 1
    cv2.drawContours(frame, [contours[max_area_index]], -1, (0,0,255), 2)
    cv2.imshow('Processed', frame)
    time.sleep(0.02)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
