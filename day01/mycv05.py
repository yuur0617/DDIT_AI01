import cv2

img = cv2.imread('winner.jpg')

(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated_45 = cv2.warpAffine(img, M, (w, h))

cv2.imshow('winner1', img)
cv2.imshow('winner2', rotated_45)

cv2.waitKey(0)
cv2.destroyAllWindows()


