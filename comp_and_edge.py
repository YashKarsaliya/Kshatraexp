import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob

def align(refx,refy,x1,y1,image):
    img = cv2.imread(image)
    rows, cols,channels = img.shape
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

def edge_nd_avg(image):
    #img = cv2.imread(image)
    edges = cv2.Canny(image,200,300)
    edge_img = np.mean(edges)
    return edge_img


master_img = '/home/yash/Documents/DOI/master/Anna2.bmp'
excel_path = '/home/yash/Documents/DOI/points.csv'
path = "/home/yash/Documents/DOI/Anna"
df = pd.read_csv(excel_path)
refx, refy = df['midx'].iloc[0], df['midy'].iloc[0] # taking reference point

df = df[1:] # removing master reference

img_path = glob.glob(path)
img_name = []
avg_all = []
crped_img = []
#split image name
for img in img_path:
    img_n = img.split('/')[-1]
    img_name.append(img_n)

#aligning all image
for i in range(len(df.index)):
    img = df['File name'].iloc[i]
    #print(img)
    img = f'{path}/{img}'
    avg_all.append(avg(img))
    x1, y1 = df['midx'].iloc[i], df['midy'].iloc[i]
    crped_img.append(align(refx,refy,x1,y1,img))

#taking edge and avg of all aligned image
ls_crop_edge = []
for i in range(len(crped_img)):
    ls_crop_edge.append(edge_nd_avg(crped_img[i]))
#master image edge detection and avg
m_i = cv2.imread(master_img)
mas_edge = edge_nd_avg(m_i)

#total average
s=0
for i in ls_crop_edge:
    s = s+i
total_avg = s/len(ls_crop_edge)

#avg diffrence w.r.t total avg
img_each = []
for i in range(len(ls_crop_edge)):
    img_each.append(total_avg - ls_crop_edge[i])

#avg diffrence w.r.t master avg
img_c_m = []
for i in range(len(ls_crop_edge)):
    img_c_m.append(mas_edge - ls_crop_edge[i])

