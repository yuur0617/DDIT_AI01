import cv2

img = cv2.imread('common_ir.png', -1)

cv2.imshow('common_ir', img)

print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()


