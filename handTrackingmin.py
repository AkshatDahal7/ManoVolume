import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=4,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
lineOnHands = mp.solutions.drawing_utils

landmark_spec = lineOnHands.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4)  # Green dots
connection_spec = lineOnHands.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2) # conncections

pTime = 0
cTime = 0 
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)



    if result.multi_hand_landmarks:
        for oneH in result.multi_hand_landmarks:
            for id ,lm in enumerate(oneH.landmark):
                h,w,c  = img.shape
                cx , cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
            lineOnHands.draw_landmarks(img,oneH,mpHands.HAND_CONNECTIONS, landmark_spec,connection_spec)


    cTime = time.time()
    frate = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(frate)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,255))
    cv2.imshow("Image",img)
    cv2.waitKey(1)