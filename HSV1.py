import cv2
import numpy as np

def nothing(x):
    pass

def ObjDetect():
    ''' Object detection
    Detect colored balls'''
    #cv2.namedWindow("Tracking")

    while True:
        frame = cv2.imread('smarties.png', 1)
        # converting to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # find the lower and upper bound for blue color
        l_b = np.array([110, 50, 50])
        u_b = np.array([130, 255, 255])
        #masking the range
        mask1 = cv2.inRange(hsv,l_b,u_b)

        # taking bitwise and on original image and applying mask to detect blue color only
        res = cv2.bitwise_and(frame, frame, mask = mask1)

        cv2.imshow("frame", frame)
        cv2.imshow("Mask", mask1)
        cv2.imshow("Resulting", res)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyAllWindows()

def ObjDetectwithTrack():
    ''' Object detection
    Detect colored balls
    It is hard to find lower bound and upper bound so we are using trackbar here'''
    cv2.namedWindow("Tracking")
    cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)   # lower Heu  (H of HSV)
    cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)  # lower Saturation
    cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)  # lower Value
    cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)  # upper Heu
    cv2.createTrackbar("US", "Tracking", 255, 255, nothing)  # upper Saturation
    cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)  # Upper Value

    while True:
        frame = cv2.imread('smarties.png', 1)
        # converting to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #get the values from trackbar
        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")
        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")
        # find the lower and upper bound for blue color
        l_b = np.array([l_h, l_s, l_v])
        u_b = np.array([u_h, u_s, u_v ])
        #masking the range
        mask1 = cv2.inRange(hsv,l_b,u_b)

        # taking bitwise and on original image and applying mask to detect blue color only
        res = cv2.bitwise_and(frame, frame, mask = mask1)

        cv2.imshow("frame", frame)
        cv2.imshow("Mask", mask1)
        cv2.imshow("Resulting", res)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyAllWindows()

def ObjDetectwithTrackVideo():
    ''' Object detection
    Detect colored balls
    It is hard to find lower bound and upper bound so we are using trackbar here'''
    cap = cv2.VideoCapture(0);
    cv2.namedWindow("Tracking")
    cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)   # lower Heu  (H of HSV)
    cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)  # lower Saturation
    cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)  # lower Value
    cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)  # upper Heu
    cv2.createTrackbar("US", "Tracking", 255, 255, nothing)  # upper Saturation
    cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)  # Upper Value

    while True:
        _,frame = cap.read()
        #frame = cv2.imread('smarties.png', 1)
        # converting to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #get the values from trackbar
        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")
        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")
        # find the lower and upper bound for blue color
        l_b = np.array([l_h, l_s, l_v])
        u_b = np.array([u_h, u_s, u_v ])
        #masking the range
        mask1 = cv2.inRange(hsv,l_b,u_b)

        # taking bitwise and on original image and applying mask to detect blue color only
        res = cv2.bitwise_and(frame, frame, mask = mask1)

        cv2.imshow("frame", frame)
        cv2.imshow("Mask", mask1)
        cv2.imshow("Resulting", res)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()