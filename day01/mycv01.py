import cv2

img = cv2.imread('woozi.jpg')
img2 = cv2.imread('woozi.jpg', 0)
img3 = cv2.imread('woozi.jpg', -1)

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)
cv2.imshow('Lena alpha channel', img3)

print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()


