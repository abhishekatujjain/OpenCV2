import numpy as np
import cv2

'''Contours are useful for shape analysis, object detection
For better accuracy we are using binary files
Before finding contours we are applying threshold or cannygradient'''
def drawContour():
    img = cv2.imread('opencv-logo-white.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # calculating the threshold
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)

    #finding the contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    ''' countours (here the variable) is a list of all the countours in the image. Each indiviudal contours
    is a NUMPY array of (x,y) coordinates of boundary points of the object 
    hierachy is the image topology: we will se later
    2 param: Contour mode
    3rd param:  contours approxiation method '''
    print("number of contours = ", str(len(contours)))
    print(contours[0])  #printing one sample countour

    cv2.drawContours(img, contours, -1, (0,0,255), 3)
    # -1 : means all countours, otherwise we can give 0 to n-1 number of contours
    # 4th param: color, 5: thickness


    cv2.imshow('Image', img)
    cv2.imshow('Gray Image', imgray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()