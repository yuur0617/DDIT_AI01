import cv2

img = cv2.imread('woozi.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('woozi', img_gray)


print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()


