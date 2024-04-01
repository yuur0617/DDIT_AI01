import cv2

img = cv2.imread('team.png')
resize_img = cv2.resize(img, (1000,750))
cv2.imshow('team', resize_img)
cv2.imwrite('team.jpg', resize_img)

cv2.waitKey(0)
cv2.destroyAllWindows()