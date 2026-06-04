import cv2
import time
import HandsTrackingModule as htm

wCam, hCam = 1080, 720

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.75, maxHands=2)

tipIds = [4, 8, 12, 16, 20]


def getGesture(fingers):
    if fingers == [0, 0, 0, 0, 0]: return "Fist"
    if fingers == [1, 1, 1, 1, 1]: return "Open Hand"
    if fingers == [0, 1, 1, 0, 0]: return "Peace"
    if fingers == [1, 0, 0, 0, 0]: return "Thumbs Up"
    if fingers == [0, 1, 0, 0, 0]: return "Pointing"
    if fingers == [0, 1, 0, 0, 1]: return "Rock On"
    if fingers == [1, 1, 0, 0, 0]: return "Gun"
    if fingers == [0, 0, 0, 0, 1]: return "Pinky"
    return ""


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    allHands = detector.findAllHands(img)

    grandTotal = 0

    if len(allHands) != 0:
        for hand in allHands:
            lmList = hand['lmList']
            side   = hand['side']
            fingers = []

            # Thumb
            if side == 'Left':
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)
            grandTotal += totalFingers

            # Gesture detection
            gesture = getGesture(fingers)

            # Per-hand label above wrist
            wrist = lmList[0]
            cv2.putText(img, f'{totalFingers}', (wrist[1] - 30, wrist[2] - 20),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            # Gesture label below wrist
            if gesture:
                cv2.putText(img, gesture, (wrist[1] - 40, wrist[2] + 40),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Total count
        cv2.putText(img, str(grandTotal), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    5, (255, 0, 255), 10)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()