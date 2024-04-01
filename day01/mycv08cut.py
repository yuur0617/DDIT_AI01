import cv2

img = cv2.imread('winner.jpg')
x = 500
y = 500
w = 500
h = 500 

croupped_img = img[y:y+h, x:x+w]

cv2.imshow('winner', img)
cv2.imshow('winner_C', croupped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


