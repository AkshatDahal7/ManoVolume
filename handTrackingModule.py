import cv2
import mediapipe as mp
import time

class HandTrackerModel:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=4,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.lineOnHands = mp.solutions.drawing_utils
        self.landmark_spec = self.lineOnHands.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4)
        self.connection_spec = self.lineOnHands.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2)

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.lineOnHands.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def drawHands(self, img):
        if self.results.multi_hand_landmarks:
            for oneH in self.results.multi_hand_landmarks:
                for id, lm in enumerate(oneH.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx, cy)
                self.lineOnHands.draw_landmarks(
                    img, oneH, self.mpHands.HAND_CONNECTIONS,
                    self.landmark_spec, self.connection_spec
                )
        return img
    def findPosition(self, img, handNo=0, draw=True):
        # xList = []
        # yList = []
        bbox = []
        self.lmList = []

        if self.results.multi_hand_landmarks:


            for hands in self.results.multi_hand_landmarks:
                h,w,c = img.shape
                lm = hands.landmark[12]

                cx,cy = int(lm.x*w), int(lm.y*h)
                self.lmList.append([12,cx,cy])
             
            # myHand = self.results.multi_hand_landmarks[handNo]
            # for id, lm in enumerate(myHand.landmark):
            #     h, w, c = img.shape
            #     cx, cy = int(lm.x * w), int(lm.y * h)
                # xList.append(cx)
                # yList.append(cy)
            #     self.lmList.append([id, cx, cy])
            #     if draw:
            #         cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            # xmin, xmax = min(xList), max(xList)
            # ymin, ymax = min(yList), max(yList)
            # bbox = xmin, ymin, xmax, ymax

            if draw:
                cv2.circle(img, (cx, cy), 8, (255, 0, 255), cv2.FILLED)

        return self.lmList

def main():
    cap = cv2.VideoCapture(0)
    handTracker = HandTrackerModel()
    pTime = 0

    while True:
        success, img = cap.read()
        result = handTracker.findHands(img)
        img = handTracker.drawHands(img)

        cTime = time.time()
        frate = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(frate)), (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 2)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()