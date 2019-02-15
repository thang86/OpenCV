import argparse
import  cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Duong dan den hinh anh')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
print('Width: {} pixel'.format(image.shape[1]))
print('Height: {} pixel'.format(image.shape[0]))
print('Channels: {} '.format(image.shape[2]))
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

