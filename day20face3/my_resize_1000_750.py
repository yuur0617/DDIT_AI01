import cv2

import cv2

image = cv2.imread('team.png')
resize_img = cv2.resize(image, (1000, 750))
cv2.imshow('resize_img',resize_img)

cv2.imwrite('team.jpg', resize_img)

cv2.waitKey(0)
cv2.destroyAllWindows()



