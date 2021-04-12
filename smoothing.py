import cv2
import numpy as np
from matplotlib import pyplot as plt

''' Smoothing also known as blurring
Most common operation to remove noise from the images
We apply lots of filters like, Homogenous filter, Gaussian, Median, Bilateral.
'''


def HomoFilter():
    ''' Most simple filter, Each output pixel is the mean of its kernel filter
    All pixels have same weights therefore  homogenous
    Kernel in Homogenous is  [1/(Kernel_Widht * Kernel_Height)] [ Ones Matrix ] '''
    #img = cv2.imread('opencv-logo-white.png', 1)
    #img = cv2.imread('img.png', 1)   # salt and pepper noise
    img = cv2.imread('lena.jpg', 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    kernel = np.ones((5, 5), np.float32)/25
    dst = cv2.filter2D(img, -1, kernel)  # 2D convolution
    #applying homogenous filter with kernel, 2nd parameter desired depth = -1
    # we get the blurred image with edges are smoothened

    ''' In one dimension Low Pass Filter helps in removing noises, blurring
    and High pass filters helps in edge detection'''

    # lets apply blur function from CV2, it is just averaging
    blur = cv2.blur(img, (5,5)) # 5,5 is a kernel of ones, output looks similar to filtering i.e. 2D convlution

    #Gaussian Filter: using different weights in x and y directions
    # Higher weights in Center, normally distributed
    gblur = cv2.GaussianBlur(img, (5, 5), 0)  # third parameter std deviation sigma

    #Median Filter: Replaces each pixel value with the median of its neighboring pixels.
    # This method is great when dealing with 'salt and pepper  noise' ( some white pixels and black pixels i.e. noise
    median = cv2.medianBlur(img, 5)  # kernel size must be odd, except 1,1 otherwise gives same image

    ''' Using above methods we removed the noise and dissolve the edge
    But when we want to keep our edges sharp we use Bilateral Filters'''
    bilateralFilter = cv2.bilateralFilter(img,9, 75, 75)
    # second param: 9, diameter of pixel 3: Sigma color, 4: Sigma Space
    ''' https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga9d7064d478c95d60003cf839430737ed'''
    titles = ['image', '2D Convolution', 'Blur', 'Gblur', 'Median Filter', 'Bilateral']
    images = [img, dst, blur, gblur, median, bilateralFilter]
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

