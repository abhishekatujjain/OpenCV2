import cv2
import numpy as np

def shapeDetect():
    img = cv2.imread('shapes.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #calculate threshold
    _, thresh = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
        #creating the polygon,  archlength= find the countour's arc length
        # since it is closed shape so arch length is true and last param is again true
        # for closed shapes

        cv2.drawContours(img, [approx], 0, (0,0,0), 5)
        ''' becoz we are iterating in the loop by contour, so index will be the first i.e. index no 0
        i.e. we are working with only one contour
        4th param is color, 5th is thickenss'''

        #printing the shapes, so we have to find the x,y coordinates
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        # since, approxPolyDP returns no of arcs, lets say 3 for traingle, 4 for rect
        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspectratio = float(w)/h
            if aspectratio > 0.95 and aspectratio < 1.05:  # ideally it should be one, but room for noise
                cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
            else:
                cv2.putText(img, "Rectangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
        elif len(approx) == 5:
            cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
        elif len(approx) == 10:
            cv2.putText(img, "Star", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
        else:
            cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv2.imshow('shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
