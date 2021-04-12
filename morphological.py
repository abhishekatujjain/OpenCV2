import cv2
from matplotlib import pyplot as plt
import numpy as np

'''
Morphological transformations are the transformation done on image shapes
We need binary images for that
A kernel tells you how to change the value of any given pixel by combining it with different amounts of neighboring pixesl

'''
def transform1():
    img = cv2.imread('smarties.png', 0) # reading in grayscale becoz binary needed, we can repalce 0 by cv2.IMREAD_GRAYSCALE
    _, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)  # if img is binary no need to apply mask, simply pass img in place of mask
    ''' While looking the output
    Original Images have some shines on the ball
    Applying inverse threshold, these shines remains black one
    to remove these black spot, we are applying cv2.dilate
    one parameter is a kernel, we will create a ones matrix of 2x2
    applying iterations, by default it is one and while iterating dots reduced and finally disappears with iterations'''

    kernel = np.ones([5,5], np.uint8)

    dilation = cv2.dilate(mask, kernel, iterations = 2)  # we can vary kernel size and iterations
    # but bigger the kernel is the size of masked shape is changed, the unwanted one so we will use erosion
    ''' Erosion is just like size erosion 
    it erodes away the boundary of foreground object
    When it is applied, the kernel we applied, slides though all the image and the pixel in the original image either 1 or 0 will be considered
    as 1 only if all pixels under the kernel is one, otherwise it is eroded i.e. value is set to 0'''

    erode = cv2.erode(mask, kernel, iterations =2)
    # another transformation is opening: It is just apply erosion on the mask and then apply dilation, i.e. dilated eroded image  dilate(erode(img))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # closing dilation is performed and then erosion, opposite of opening
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # some other methods
    mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)  # dilation - erosion
    th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel) # image - opening
    # similarly blackhat, elipse, erode, hitmiss, rectangle and so on, just change the second argument and you will get the list

    titles = ['Image', 'Mask', 'Dilation', 'Erode', 'opening', 'closing', "Gradient", 'Tophat']
    images = [img, mask, dilation, erode, opening, closing, mg, th]

    for i in range(8):
        plt.subplot(3,3, i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()