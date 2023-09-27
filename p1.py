import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('ls1.jpeg')
kernal = np.ones((2,2), np.uint8)


def eroison():
	eroison = cv2.erode(img, kernal, iterations=1)
    plt.imshow(eroison)

def dilation():
	dilation = cv2.dilate(img,kernal,iterations = 1)
    plt.imshow(dilation)
	
def opening():
	opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
    plt.imshow(opening)

def closing():
	closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)
    plt.imshow(closing)

def gradient():
	gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal)
    plt.imshow(gradient) 

def tophat():
	tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernal)
    plt.imshow(tophat)

def blackhat():
	blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernal)
    plt.imshow(blackhat)

