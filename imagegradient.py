import cv2
import numpy as np
from matplotlib import pyplot as plt

'''Image Gradient is a directional change in the intensity or color in an image
It will be used for edge detection'''

def calculategradient():
    #img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('sudoku.png', cv2.IMREAD_GRAYSCALE)
    #laplacian gradient
    lap = cv2.Laplacian(img, cv2.CV_64F, ksize= 3)
    ''' cv2.CV_64F is a data type. We are using 64 bit float due to negative slope induced by due
     transforming image from white to black. It is just a -ve float to store data
     ksize = kernel size, it is optional'''
    lap = np.uint8(np.absolute(lap))  # converting -ve value to unsigned 8 bit integer

    #sobelgradient
    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    #3rd is dx means we want to calculate gradient in direction of x, dx derivative, it is 1 or 0, if 1 then we are calcuating dx
    # 4th is dy i.e. gradient (change in intensity) in y direction dy, fifth is ksize = optional
    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

    #converting absolute
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))

    #combining both the directions
    sobelCombine = cv2.bitwise_or(sobelX, sobelY)


    titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined']
    images = [img, lap, sobelX, sobelY, sobelCombine]
    for i in range(5):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()


def cannyEdgeDetect():
    '''Canny Edge Detector is an edge detection operator that uses multistage algorithm to detect a wide range of edges
     in images. the algorithm is composed of 5 steps
     1. Noise Reduction 2. Gradient Calculation 3. Non-maximum Supression 4. Double Threshold 5. Edge tracking by Hysteresis '''
    img = cv2.imread('messi5.jpg', 0)

    canny = cv2.Canny(img, 100 , 200)  # directly pass 100, 200 as 2nd and 3rd param, no need to use trackbar
    ''' 2 and 3 parameter are threshold 1 and 2  for hysteresis process'''
    titles = ['image', 'canny']
    images = [img, canny]
    for i in range(2):
        plt.subplot(1, 2, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()
