import cv2
import numpy as np

''' Thresholding: comparing each pixel values'''

def thresh():
    img = cv2.imread('gradient.png', 0)
    _, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ''' first param: grayscale image
    second: threshold value
    third: max value of pixel
    Thresh_Binary: if pixel > threhold then pixel = max value otherwise pixel = 0'''

    _, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
    _, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    # if the  value is greater than 127 it remains 127, other wise remains unchanged


    _, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    # when the value is less than threshold (127 here), it changed to 0 otherwise remains unchanged
    _, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('image', img)
    cv2.imshow('threhold', th1)
    cv2.imshow('threholdInv', th2)
    cv2.imshow('threholdTrunc', th3)
    cv2.imshow('threholdToZeor', th4)
    cv2.imshow('threholdToZeroInv', th5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def adaptivethresh():
    ''' in the previous function, we are applying threshold to all the pixel
    but  we want to apply on different regions
    NOw we are calculating threshold will be calculating threshold on smaller regions
    different threshold values for different regions
    Need: In images, various lighting conditions in different regions so we need adaptive thresholding'''
    img = cv2.imread('sudoku.png', 0)
    _, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # adaptive one
    th2 = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2);
    # img = source, 255 = max value, 3rd param = taking mean of neighboring pixels
    # 4th: type of threshold, 5th: Block size: size of neighboring area
    # 7: C is the constant is minus from mean (Bias)

    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow("image",img)
    cv2.imshow("Binary", th1)
    cv2.imshow("Adaptive_Binary", th2)
    cv2.imshow("Adaptive_Gaussian", th3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()