import cv2
import  argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Duong dan den anh')

args = vars(ap.parse_args())

image= cv2.imread(args['image'])

cv2.imshow('Original',image)
(b,g,r) = image[0,0]
print('Pixel at (0,0) Red {}, Green {}, Blue {}'.format(r,g,b))

image[0,0] = (0,0,255)
(b,g,r) = image[0,0]
print('Pixel at (0,0) Red {}, Green {}, Blue {}'.format(r,g,b))

coner = image[0:250,0:250]
cv2.imshow('conner',coner)
image[0:250,0:250] = (0,0,255)
cv2.imshow('update',image)
cv2.waitKey(0)

