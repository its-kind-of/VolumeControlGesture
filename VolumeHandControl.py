import cv2
import mediapipe as mp
import numpy as np
import time
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

##################################
# camera width and height
wCam, hCam = 648, 480
##################################

cap = cv2.VideoCapture(0)
#cap.set(3, wCam)
#cap.set(4, hCam)
pTime = 0

detector = htm.HandDetector(detectionCon=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

while True :
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        #print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        circle_size = 10
        cv2.circle(img, (x1, y1), circle_size, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), circle_size, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), circle_size, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        #print(length)
        #cv2.putText(img, str(length), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)

        # Hand Range 25 - 180
        # Volume Range - 96 - 0
        vol = np.interp(length, [25, 160], [minVol, maxVol])
        volBar = np.interp(length, [25, 180], [400, 150])
        volPer = np.interp(length, [25, 180], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), circle_size, (0, 255, 0), cv2.FILLED)

        if length > 140:
            cv2.circle(img, (cx, cy), circle_size, (0, 0, 255), cv2.FILLED)

    cv2.rectangle(img, (50, 50), (85, 400), (255,0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255,0, 0), cv2.FILLED)
    cv2.putText(img, f"Volume : {int(volPer)}", (40, 440), cv2.FONT_HERSHEY_PLAIN, 1, (255,0, 0), 1)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS : {int(fps)}", (40, 40), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)
    cv2.imshow("Img", img)
    cv2.waitKey(1)