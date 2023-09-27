import pandas as pd
import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


class Image:

    def __init__(self) -> None:
        pass   
            
    def get_block(self,image,row,column):
        # img = cv2.imread(image,0)
        ht, wd = image.shape
        ch = 0 
        cw = 0
        nh = ht//row
        nw = wd//column
        ls = []
        m = nh

        if cw == 0:
            cri = image[ch:nh,cw:nw]
            # print(type(cri))
            ls.append(cri)
        n = nw
        for j in range(2,column+1):
            cw = nw
            nw = n*j
            cri = image[ch:nh,cw:nw]
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
                    cri = image[ch:nh,cw:nw]
                    ls.append(cri)
                n = nw
                for j in range(2,column+1):
                    cw = nw
                    nw = n*j
                    cri = image[ch:nh,cw:nw]
                    ls.append(cri)
            #i = i+1
        return ls 

    def avg_block_diff(self,block1,block2):
        ht1 , wd1 = block1.shape
        ht2 , wd2 = block2.shape

        a = np.mean(block1)
        b = np.mean(block2)
        avg = a - b
        return avg


    def align(self,refx,refy,x1,y1,img):
        rows, cols = img.shape
        if (refx==x1) and (refy==y1):
            #print('Same')
            return img
            #plt.imshow(img)
        else:
            difx= refx - x1
            dify = refy - y1
            if (dify>0):
                crop_img = img[0:rows,(cols-dify):cols]
                img = img[0:rows,0:(cols-dify)]
                im_h = cv2.hconcat([crop_img, img])
                #plt.imshow(im_h)
                img = im_h
                #return im_h
            elif (dify<0):
                dify = abs(dify)
                crop_img = img[0:rows,0:dify]
                img = img[0:rows,dify:cols]
                im_h = cv2.hconcat([img,crop_img])
                img = im_h
                #plt.imshow(im_h)
                #return im_h
            if (difx>0):
                crop_img = img[0:difx,0:cols]
                img = img[difx:rows,0:cols]
                im_v = cv2.vconcat([img,crop_img])
                img = im_v
                #plt.imshow(im_v)
                #return im_v
            elif (difx<0):
                difx = abs(difx)
                crop_img = img[(rows-difx):rows,0:cols]
                img = img[0:(rows-difx),0:cols]
                im_v = cv2.vconcat([crop_img, img])
                img = im_v
                #plt.imshow(im_v)
            return img

def main():

    obj = Image()

    excel_path = '/home/office5/Desktop/TESTING/points.csv'
    df = pd.read_csv(excel_path)

    # Aligninig image
    crped_img = []
    lst = []
    height,width = 4,3 
    path = '/home/office5/Desktop/TESTING/'
    refx, refy = df['midx'].iloc[0], df['midy'].iloc[0]


    print('Here time Used for alignment')
    start2 = time.time()

    for i in range(len(df.index)):
        img = df['File name'].iloc[i]
        img = f'{path}/{img}'
        x1, y1 = df['midx'].iloc[i], df['midy'].iloc[i]
        img = cv2.imread(img,0)
        crped_img.append(obj.align(refx,refy,x1,y1,img))
        each_blk = obj.get_block(crped_img[i],height,width)
        lst.append(each_blk)

    end2 = time.time()
    print("time for generating alignment image ",end2 - start2)
    # print(crped_img[0][1][1])
        
    print("Here time used for generating master Image")
    start1 = time.time()

    hei,wid = crped_img[0].shape
    master_img = np.zeros([hei, wid])
    # for i in range(hei):
    #     for j in range(wid):
    #         master_img[i,j] = 0
    #         for k in range(len(df.index)):
    #             master_img[i,j] += (int(crped_img[k][i,j]))
    #         master_img[i,j] = master_img[i,j] / len(crped_img)

    N = len(crped_img)

    for im in crped_img:
        imarr=np.array(im)
        master_img=master_img+imarr/N

    end1 = time.time()
    print("time for generating master image ",end1 - start1)

    ac = []
    ac.append(obj.get_block(master_img,height,width))

    print('Here to get difference between master image and rest other image')
    for i in range(len(lst)):
        start = time.time()
        lst1 = []
        for j in range(len(lst[1])):
            lst1.append(obj.avg_block_diff(ac[0][j],lst[i][j]))
        print(f"Difference between master_img and {df['File name'].iloc[i]}")
        end = time.time()
        print("time difference is ",end - start)
        print(lst1)
        print('\n')

main()






