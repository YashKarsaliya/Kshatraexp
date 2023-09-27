import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)
cap.set(cv2.CAP_PROP_FPS, 60)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


# cTime = 0

while(True):
    pTime = time.time()
    succsess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    one = cv2.rectangle(img, (1100, 70), (1200, 170), (255, 255, 0), cv2.FILLED)
    two = cv2.rectangle(img, (900,70), (1000, 170), (2,10, 200), cv2.FILLED)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                if id == 8:
                    cv2.circle(img, (cx, cy), 10, (255,0,0), cv2.FILLED)

                if id == 8 and id == 12:
                    cv2.rectangle(img, (cx, cy), (10, 10), (255,0,0), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            mpDraw.RED_COLOR

        cTime = time.time()
        gt = cTime - pTime
        gt = gt*1000
        print("gt is:",gt)

        # fps = 1 / (cTime - pTime)
        # pTime = cTime



    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()