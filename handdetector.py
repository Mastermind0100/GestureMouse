import mediapipe as mp
import cv2

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

class HandDetector:
    def __init__(self, max_num_hands = 2, min_detection_confidence = 0.7, min_tracking_confidence = 0.5):
        self.hands = mpHands.Hands(max_num_hands = max_num_hands, min_detection_confidence=min_detection_confidence,
                                    min_tracking_confidence = min_tracking_confidence)

    def findHandLandMarks(self, image, handNumber=0, draw=False):
        original_image = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image)
        landMarkList = []
        imgH, imgW, imgC = original_image.shape

        if results.multi_hand_landmarks: 
            hand = results.multi_hand_landmarks[handNumber]

            for id, landmark in enumerate(hand.landmark):
                xPos, yPos = int(landmark.x*imgW), int(landmark.y*imgH)
                landMarkList.append([id, xPos, yPos])
            
            if draw:
                mpDraw.draw_landmarks(original_image, hand, mpHands.HAND_CONNECTIONS)
            
        return landMarkList
