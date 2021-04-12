import cv2
import numpy as np

def basicMotionDetection():
    cap = cv2.VideoCapture('vtest.avi')
    #cap = cv2.VideoCapture(0)
    # caputuring only two frame, if we need all, then we put it in while loop, i commented all frame there
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while cap.isOpened():
        #ret, frame = cap.read()   # we don't need this

        # finding absolute difference between first two frames
        diff =  cv2.absdiff(frame1, frame2)

        #converting difference into grayscale to easily find contours
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations= 3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
        #why i commented this becoz it creates contours, and also includes noise,
        # i want rectangle and want to remove noise too

        for contour in contours:
            (x,y,w,h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 700:
                continue
            cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame1,"Status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
        cv2.imshow("inter", frame1)

        frame1 =frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(40) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()