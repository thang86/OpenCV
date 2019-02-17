import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Duong dan den hinh anh")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("anh_goc", image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("anh_den_trang", image)

# image
# threshold1
# threshold2
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Result", canny)
cv2.waitKey(0)