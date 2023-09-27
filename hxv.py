import cv2
import numpy as np
import time
import HandTrackingModule as htm

pt = time.time()

vid = cv2.VideoCapture(0)

vid.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)
vid.set(cv2.CAP_PROP_FPS, 60)
detector = htm.hand_tracker(detectionCon=0.85)
tipIds = [4, 8, 12, 16, 20]


while True:
    ret, img = vid.read()
    img = detector.find_hands(img)
    lmList = detector.find_position(img, draw=False)
    cv2.rectangle(img,(600,70),(800,270),(255, 255, 0), cv2.FILLED)
    # if cv2.waitKey(1) & 0xFF == ord('w'):
    #cv2.putText(img,f'band-1', (600, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 0, 0), 3)
    #if cv2.waitKey(1) & 0xFF == ord('a'):
    # for i in range(len(ls)):
    #     cv2.putText(frame,ls[i],(600, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (128, 0, 0), 3)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = []

        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 6):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

            i = 0
            if fingers[1] :
                count = i + 1
                cv2.putText(img, f'band-{count}', (600, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 0, 0), 3)


        # if fingers[1] and fingers[2] == False:
        #     cv2.circle(img, (x1, y1), 15, (0,0,255), cv2.FILLED)
        #     print("drawing mode")
        #     if p1==0 and p2==0:
        #         p1, p2 = x1, y1

    # Display the resulting frame
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

