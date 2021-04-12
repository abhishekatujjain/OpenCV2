import cv2
from matplotlib import pyplot as plt

def simpleplot():
    img = cv2.imread("lena.jpg",1)
    cv2.imshow("image",img)  # uses BGR format

    #plt.imshow(img)
    # it reads image in RGB format, we need to convert the format

    #plt.show()

    # convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    #plt.xticks([]), plt.yticks([])     # to hide the ticks from matplotlib image
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def plotwiththreshold():
    img = cv2.imread('gradient.png',0)
    _, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    _, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
    _, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    _, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    _, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    titles = ['Original Image', 'Binary', 'Binary Inv', 'Trunc', 'To Zero', 'To Zero Inv']
    images = [img, th1, th2, th3, th4, th5]

    for i in range(6):
        plt.subplot(2,3,i+1)  # divide plot in 2 rows, 3 columns and i+1 in number
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()