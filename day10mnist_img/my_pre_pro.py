import cv2

img = cv2.imread('9.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_28 = cv2.resize(img_gray,(28,28))

cv2.imshow('9', img_gray_28)

print(img_gray_28.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


