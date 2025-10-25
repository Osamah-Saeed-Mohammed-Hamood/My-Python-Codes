import cv2
import numpy as np

img=cv2.imread('d:\Osama Al-Jabali\Osama2.jpg')
new_img=np.zeros(img.shape,dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b=img[i,j,0]
        g=img[i,j,1]
        r=img[i,j,2]
        if(not ((120<b<195) and (140<g<190) and (180<r<230))):
                    # if(not ((20<b<180) and (34<g<210) and (45<r<255))):
            new_img[i,j,:]=255

cv2.imshow('Origin',img)
cv2.imshow('new',new_img)
cv2.waitKey()
cv2.destroyAllWindows()
