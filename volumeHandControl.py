import cv2
import time
import numpy as np
import handTrackingModule as htm
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
cap = cv2.VideoCapture(0)
wCam , hCam = 640,480

cap.set(3,wCam)
cap.set(4, hCam)
pTime = 0
cTime = 0

detector = htm.HandTrackerModel()

from pycaw.pycaw import AudioUtilities
device = AudioUtilities.GetSpeakers()
interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Cast the interface to IAudioEndpointVolume
volume = interface.QueryInterface(IAudioEndpointVolume)


while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList)>=2:
        x1,y1 = lmList[0][1],lmList[1][2]
        x2,y2 = lmList[1][1], lmList[1][2]
        distance = math.hypot(x2-x1,y2-y1)
        
        minDist = 20    
        maxDist = 200  

        distance = max(min(distance, maxDist), minDist)

        minVol, maxVol, _ = volume.GetVolumeRange() 
        vol = np.interp(distance, [minDist, maxDist], [minVol, maxVol])
        print(vol)
        volume.SetMasterVolumeLevel(vol, None)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img , f'{int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    cv2.imshow("IMG", img)
    cv2.waitKey(1)