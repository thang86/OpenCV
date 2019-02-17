import cv2
import numpy as np
import  argparse
import  imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Duong dan den hinh anh')

args = vars(ap.parse_args())

image =cv2.imread(args['image'])
num_rows,num_cols = image.shape[:2]

cv2.imshow('Anh goc',image)

M = np.float32([[1,0,70],[0,1,110]])
img_translation = cv2.warpAffine(image,M,(num_rows,num_cols))
img_translations = cv2.warpAffine(image,M,(num_rows+70,num_cols+110))
cv2.imshow('Tren-Xuong',img_translation)
cv2.imshow('Tren-Xuongx',img_translations)

cv2.waitKey(0)