import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob

# img1 = input('')        #image path
# img2 = input('')        #image path
# image1 = cv2.imread(img1)
# image2 = cv2.imread(img2)


path = glob.glob("/home/yash/Documents/DOI/Anna/*.bmp")
cv_img = []
for img in path:
    n = cv2.imread(img)
    cv_img.append(n)

def CompareImage(image1,image2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    orig = cv2.resize(img1,(600,300))
    imc = cv2.resize(img2,(600,300))
    subtract = cv2.subtract(orig,imc)
    height, width = subtract.shape
    a = []
    for x in range(0,height):
        for y in range(0,width):
            if (subtract[x,y] > 0):
                a.append(subtract[x,y])
            else:
                pass
    np.asarray(a)
    return len(a)

  

def KeyPoints(image1,image2):
    img1 = cv2.imread('index1.jpeg')
    img2 = cv2.imread('index2.jpeg')
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    kp = sift.detect(gray1,None)
    img=cv2.drawKeypoints(gray1,kp,gray2)
    plt.imshow(img)    


def edge(img):
    img = cv2.imread(img)
    edges = cv2.Canny(img,200,300)
    plt.imshow(edges, cmap='gray')