import cv2
import pyautogui as pag
import handdetector as hdr

pag.FAILSAFE = False

if __name__ == '__main__':
    handDetector = hdr.HandDetector()
    screen_x, screen_y = pag.size()
    multiplier_x = screen_x/640             #this is the resolution of my camera (480x640)
    multiplier_y = screen_y/480             #You will have to change according to your own
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, inp_frame = cap.read()
        frame = cv2.flip(inp_frame, 1)
        handLandmarks = handDetector.findHandLandMarks(image = frame, draw = True)
        if len(handLandmarks)==0:
            continue
        x_crdnt, y_crdnt = handLandmarks[8][1], handLandmarks[8][2]
        cv2.circle(frame, (x_crdnt, y_crdnt), 5, (0,255,255), -1)
        cv2.imshow('frame', frame)                                          # You can comment this line out to not show your webcam output
        pag.moveTo(int(x_crdnt*multiplier_x), int(y_crdnt*multiplier_y), duration = 0.01)
        
        if cv2.waitKey(1) & 0xff == 27:
            break
    
    cv2.destroyAllWindows()
    cap.release()
