import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('ls1.jpeg')
kernal = np.ones((2,2), np.uint8)

class Morph:    
    def eroison():
        eroison = cv2.erode(img, kernal, iterations=1)
        plt.title('Eroison')
        plt.imshow(eroison)

    def dilation():
        dilation = cv2.dilate(img,kernal,iterations = 1)
        plt.title('Dilation')
        plt.imshow(dilation)

    def opening():
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
        plt.title('Opening')
        plt.imshow(opening)

    def closing():
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)
        plt.title('Closing')
        plt.imshow(closing)

    def gradient():
        gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal)
        plt.title('Gradient')
        plt.imshow(gradient) 

    def tophat():
        tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernal)
        plt.title('Tophat')
        plt.imshow(tophat)

    def blackhat():
        blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernal)
        plt.title('Blackhat')
        plt.imshow(blackhat)
        
    def plotall():
        plt.figure(figsize=(20, 20))
        plt.subplot(1, 7, 1)
        Morph.eroison()
        plt.subplot(1, 7, 2)
        Morph.dilation()
        plt.subplot(1, 7, 3)
        Morph.opening()
        plt.subplot(1, 7, 4)
        Morph.closing()
        plt.subplot(1, 7, 5)
        Morph.gradient()
        plt.subplot(1, 7, 6)
        Morph.tophat()
        plt.subplot(1, 7, 7)
        Morph.blackhat()