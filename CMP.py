import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob 

def get_block(image,row,column):
    img = cv2.imread(image)
    ht, wd, ch = img.shape
    ch = 0 
    cw = 0
    nh = ht//row
    nw = wd//column
    ls = []
    m = nh
    #for i in range(0,row):
    if cw == 0:
        cri = img[ch:nh,cw:nw]
        ls.append(cri)
    n = nw
    for j in range(2,column+1):
        cw = nw
        nw = n*j
        cri = img[ch:nh,cw:nw]
        ls.append(cri) 
    for i in range(0,row):
        if i > 0:
            rc = i+1
            #print(i)
            ch = nh
            nh = m * rc
            cw = 0
            nw = nw//column
            if cw == 0:
                cri = img[ch:nh,cw:nw]
                ls.append(cri)
            n = nw
            for j in range(2,column+1):
                cw = nw
                nw = n*j
                cri = img[ch:nh,cw:nw]
                ls.append(cri)
        #i = i+1
    return ls

def CP(refx,refy,x1,y1,image):
    img = cv2.imread(image)
    rows, cols,channels = img.shape
    if (refx==x1) and (refy==y1):
        print('Same')
        plt.imshow(img)
    else:
        difx= refx - x1
        dify = refy - y1
        if (dify>0):
            crop_img = img[0:rows,(cols-dify):cols]
            img = img[0:rows,0:(cols-dify)]
            im_h = cv2.hconcat([crop_img, img])
            #plt.imshow(im_h)
            return im_h
        elif (dify<0):
            dify = abs(dify)
            crop_img = img[0:rows,0:dify]
            img = img[0:rows,dify:cols]
            im_h = cv2.hconcat([img,crop_img])
            #plt.imshow(im_h)
            return im_h
        if (difx>0):
            crop_img = img[0:difx,0:cols]
            img = img[difx:rows,0:cols]
            im_v = cv2.vconcat([img,crop_img])
            #plt.imshow(im_v)
            return im_v
        elif (difx<0):
            difx = abs(difx)
            crop_img = img[(rows-difx):rows,0:cols]
            img = img[0:(rows-difx),0:cols]
            im_v = cv2.vconcat([crop_img, img])
            #plt.imshow(im_v)
            return im_v
        
def avg_block_diff(block1,block2):
    blok1 = cv2.cvtColor(block1, cv2.COLOR_BGR2GRAY)
    blok2 = cv2.cvtColor(block2, cv2.COLOR_BGR2GRAY)
    height1 , width1 = blok1.shape
    height2 , width2 = blok2.shape
    list1 = []
    list2 = []
    # x, y for particular position in image1 i.e (2,3) 
    for x in range(0,height1):
        for y in range(0,width1):
            list1.append(blok1[x,y])
    
    # w, z for particular position in image2 i.e (2,3)
    for w in range(0,height2):
        for z in range(0,width2):
            list2.append(blok2[w,z])
            
    total1 = 0
    for i in range(len(list1)):
        total1 = total1 + list1[i]
        
    total2 = 0
    for j in range(len(list2)):
        total2 = total2 + list2[j]
    
    avg1 = total1/len(list1)
    avg2 = total2/len(list2)
    return avg1, avg2