import cv2

img = cv2.imread('winner.jpg')

cv2.imshow('winner', img)
cv2.imwrite("winner.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


