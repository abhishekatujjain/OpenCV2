import cv2
import numpy as np


''' If we have to work with images of different sizes
Let's say we have to find face in the image
Pyramid representation is a type of multiscale signal representation in which a signal
or an image is subject to repeated smoothing and subsampling
There are 2 types of pyramids are available in OpenCV
1. Gaussian   2. Laplacian'''


def gaussianPyramidexample():
    ''' It is repeated filtering and subsampling of images
    two functions are available for Gaussian Pyramid
    1. Pyrdown and pyrup'''
    img = cv2.imread('lena.jpg')

    lr1 = cv2.pyrDown(img)  # we get low resolution image by 1/4
    lr2 = cv2.pyrDown(lr1)
    hr2 = cv2.pyrUp(lr2) # resolution increased but blurred and not equals to lr1
    hr1 = cv2.pyrUp(hr2)

    cv2.imshow('image', img)
    cv2.imshow('pyrDown1', lr1)
    cv2.imshow('pyrDown2', lr2)
    cv2.imshow('pyrup2', hr2)
    cv2.imshow('pyrup1', hr1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def gaussianPyramid():
    img =cv2.imread('lena.jpg')

    #creating layers i.e. pyramid
    layer = img.copy()   #image copying
    gp =  [layer]   #gausian pyarmid

    for i in range(6):
        layer = cv2.pyrDown(layer)
        gp.append(layer)
        cv2.imshow(str(i),layer)
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def laplacianPyramid():
    ''' NO exclusive methods for laplacian like pyrup and down
    It is formed by the difference between that level in Gaussian Pyramid and expanded version
    of its upper level in Gaussian Pyramid'''
    img = cv2.imread('lena.jpg')

    # creating layers i.e. pyramid
    layer = img.copy()  # image copying
    gp = [layer]  # gausian pyarmid

    for i in range(6):
        layer = cv2.pyrDown(layer)
        gp.append(layer)
        #cv2.imshow(str(i), layer)
    layer = gp[5]   # the last layer is the upper layer
    cv2.imshow("upper layer of the Gaussian pyramid", layer)
    lp = [layer]  # laplacian initianlization

    for i in range(5,0,-1):
        gaussianextended = cv2.pyrUp(gp[i])
        laplacian = cv2. subtract(gp[i-1], gaussianextended)
        cv2.imshow(str(i), laplacian)  # we get the edges, It helps to blend the images, reconstruct the images

    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imageBlending():
    ''' One of the application of Image Pyramid is Image Pyramid
    Let's say we have two images of same shape and we like to blend them'''
    apple = cv2.imread('apple.jpg')
    orange = cv2.imread('orange.jpg')

    # Now Blend the images side by side
    apple_orange = np.hstack((apple[:, :256], orange[:,256:])) # taking half of both images and stacking
    cv2.imshow("Apple_Orange", apple_orange)
    # as we can see, clear separating line is available, so we have to hide it, i.e. we like to blend it
    #so we are going to use image pyaramid techniques
    ''' So we are having 5 steps to do this
    1. Load two images of Apple and Orange
    2. Find the Gaussian Pyramids for apple and orange (in this examples, no of levels is 6
    3. From gaussian pyramid, find the laplacian pyramid
    4. Now join the left half of the apple and right half of orange in each levels of laplacian pyramids
    5. Finally, from this image, reconstruct the original image'''

    # First step is already done
    # 2nd step Generate Gaussian Pyramid
    apple_copy = apple.copy()
    gp_apple = [apple_copy]
    for i in range(6):
        apple_copy = cv2.pyrDown(apple_copy)
        gp_apple.append(apple_copy)

    orange_copy = orange.copy()
    gp_orange = [orange_copy]
    for i in range(6):
        orange_copy = cv2.pyrDown(orange_copy)
        gp_orange.append(orange_copy)

    #Generating laplaciang pyramid
    apple_copy = gp_apple[5]
    lp_apple = [apple_copy]
    for i in range(5, 0, -1):
        gaussianext = cv2.pyrUp(gp_apple[i])
        laplacian = cv2.subtract(gp_apple[i-1], gaussianext)
        lp_apple.append(laplacian)
    orange_copy = gp_orange[5]
    lp_orange = [orange_copy]
    for i in range(5,0, -1):
        gaussianext =cv2.pyrUp(gp_orange[i])
        laplacian = cv2.subtract(gp_orange[i-1], gaussianext)
        lp_orange.append(laplacian)

    #add left and right halves
    apple_orange_pyramid = []
    n = 0
    for apple_lap, orange_lap in zip(lp_apple,lp_orange):
        n+=1
        cols, rows, ch = apple_lap.shape
        laplacian = np.hstack((apple_lap[:, 0: int(cols/2)], orange_lap[:, int(cols/2):]))
        apple_orange_pyramid.append(laplacian)

    # reconstruct image
    apple_orange_re = apple_orange_pyramid[0]
    for i in range(1, 6):
        apple_orange_re = cv2.pyrUp(apple_orange_re)
        apple_orange_re = cv2.add(apple_orange_pyramid[i], apple_orange_re)

    cv2.imshow('Apple', apple)
    cv2.imshow('Orange', orange)
    cv2.imshow("Apple_Orange", apple_orange)
    cv2.imshow("Apple Orange Reconstructed", apple_orange_re)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
