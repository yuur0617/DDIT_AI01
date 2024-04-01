import cv2

img = cv2.imread('woozi.jpg')

cv2.rectangle(img, 
            (100, 50, 200, 200),
            (0,0,255),
            2)  
cv2.imshow('woozi', img)

print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()


