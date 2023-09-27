import numpy as np
import cv2
import matplotlib.pyplot as plt


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
            im_h = cv2.hconcat([crop_img, img])
            #plt.imshow(im_h)
            return im_h
        elif (dify<0):
            dify = abs(dify)
            crop_img = img[0:rows,0:dify]
            im_h = cv2.hconcat([img,crop_img])
            #plt.imshow(im_h)
            return im_h
        if (difx>0):
            crop_img = img[0:difx,0:cols]
            im_v = cv2.vconcat([img,crop_img])
            #plt.imshow(im_v)
            return im_v
        elif (difx<0):
            difx = abs(difx)
            crop_img = img[(rows-difx):rows,0:cols]
            im_v = cv2.vconcat([crop_img, img])
            #plt.imshow(im_v)
            return im_v


def slice(image):
    img = cv2.imread(image)
    ht, wd, ch = img.shape
    ch, cw = 0, 0
    nh = ht//3
    nw = wd//4
    ls = []
    m = nh
    if len(ls) < 4:
        if cw == 0:
            cri = img[ch:nh,cw:nw]
            ls.append(cri)
        n = nw
        for j in range(2,5):
            cw = nw
            nw = n*j
            cri = img[ch:nh,cw:nw]
            ls.append(cri)

        

    if len(ls) <= 4:
        ch = nh
        nh = m * 2
        cw = 0
        nw = nw//4
        if cw == 0:
            cri = img[ch:nh,cw:nw]
            ls.append(cri)
        n = nw
        for j in range(2,5):
            cw = nw
            nw = n*j
            cri = img[ch:nh,cw:nw]
            ls.append(cri)

        # if ch == 0:
        #     cri = img[ch:nh,cw:nw]
        #     ls.append(cri)

    if len(ls) == 8:
        ch = nh
        nh = m * 3
        cw = 0
        nw = nw//4
        if cw == 0:
            cri = img[ch:nh,cw:nw]
            ls.append(cri)
        n = nw
        for j in range(2,5):
            cw = nw
            nw = n*j
            cri = img[ch:nh,cw:nw]
            ls.append(cri)

        # if ch == 0:
        #     cri = img[ch:nh,cw:nw]
        #     ls.append(cri)
            
    return ls



def CI(b1,b2):
    diff = cv2.subtract(b1,b2)
    return len(diff)




def compare(blk1,blk2):
    orig = cv2.cvtColor(blk1, cv2.COLOR_BGR2GRAY)
    imc = cv2.cvtColor(blk2, cv2.COLOR_BGR2GRAY)
    #subtract = cv2.subtract(orig,imc)
    diff = cv2.subtract(orig,imc)
    height, width = diff.shape
    a = []
    for x in range(0,height):
        for y in range(0,width):
            if (diff[x,y] > 0):
                a.append(diff[x,y])
            else:
                pass
    np.asarray(a)
    return len(a)


def concat(list_2d):
    row = [cv2.hconcat(list_h) for list_h in list_2d]
    img = cv2.vconcat(row)
    return img

img_t = concat([[dif[0], dif[1], dif[2],dif[3]],
                      [dif[4], dif[5], dif[6],dif[7]],
                      [dif[8], dif[9], dif[10],dif[11]]])



# dynamic slicing of image
def sl(image,row,column):
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