import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob


class Image:

    def __init__(self) -> None:
        pass

        
    def get_block(self,image,row,column):
        img = cv2.imread(image,0)
        ht, wd = img.shape
        ch = 0 
        cw = 0
        nh = ht//row
        nw = wd//column
        ls = []
        m = nh

        if cw == 0:
            cri = img[ch:nh,cw:nw]
            print(type(cri))
            ls.append(cri)
            print(ls)
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
        np.asarray(ls)
        return ls 

    def avg_block_diff(self,block1,block2):
        ht1 , wd1 = block1.shape
        ht2 , wd2 = block2.shape

        #total1,total2 = 0,0
        avg1 = np.mean(block1)
        avg2 = np.mean(block2)
#         for x in range(0,ht1):
#             for y in range(0,wd1):
#                 total1 = total1 + block1[x,y]

#         for w in range(0,ht2):
#             for z in range(0,wd2):
#                 total2 = total2 + block2[w,z]
        
#         avg1 = total1/(ht1*wd1)
#         avg2 = total2/(ht2*wd2)
        avg = avg1 - avg2
        return avg

def main():


    lst,height,width = [],4,3

    obj = Image()

    excel_path = '/home/yash/Documents/DOI/points.csv'
    img_giv_pth = "/home/yash/Documents/DOI/Anna"
    img_pth = glob.glob(img_giv_pth)
    # img_pth = sorted(img_pth, key=lambda item: int(item.split('Anna')[1].split('.bmp')[0]))


    lst,height,width = [],4,3

    df = pd.read_csv(excel_path)

    img_name = []
    for img in img_pth:
        img_n = img.split('/')[-1]
        img_name.append(img_n)

    # 
    for i in range(len(df.index)):
        img = df['File name'].iloc[i]
        img = f'{img_giv_pth}/{img}'
        each_blk = obj.get_block(img,height,width)
        lst.append(each_blk)

    print('Here come fast')
    Difference_lst = []
    for i in range(len(lst)-1):
        lst1 = []
        for j in range(len(lst[1])):
            lst1.append(obj.avg_block_diff(lst[i][j],lst[i+1][j]))
        Difference_lst.append(lst1)
        print(f"Difference between {df['File name'].iloc[i]} and {df['File name'].iloc[i+1]}")
        print(lst1)
        print('\n')
main()