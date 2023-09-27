import cv2
# import mediapipe as mp
import time
import HandTrackingModule as htm
import math
from subprocess import call
import numpy as np

pt = 0
ct = 0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)
cap.set(cv2.CAP_PROP_FPS, 60)
tracker = htm.hand_tracker(detectionCon=0.7, maxHands=1)

vol = 0
volbar = 400
volPer = 0
while True:
    success, img = cap.read()
    img = tracker.find_hands(img)
    lmList = tracker.find_position(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 13, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 13, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 100, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        vol = np.interp(length, [50, 300], [0,100])
        volbar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])

        #call(["amixer", "-D", "pulse", "sset", "Master", str(vol)+"%"])

        if length < 25:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (255,255,0), 3)
    cv2.rectangle(img, (52, int(volbar)), (83, 400), (0,255,255), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (0,255,255), 3)
    #cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
    ls = ['band1','band2','band3','band4','band5','band6','band7','band8','band9']
    cv2.rectangle(img,(1300,170),(1800,270),(255, 255, 0), cv2.FILLED)
    #cv2.putText(img, "band1", (1850, 210), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 0, 0), 3)
    for i in range(len(ls)):
        cv2.putText(img,ls[i],(1000, 210), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 0, 0), 3)

    ct = time.time()
    fps = 1 / (ct - pt)
    pt = ct
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2,
                (0, 100, 255), 2)
    cv2.imshow('video', img)
    cv2.waitKey(1)




