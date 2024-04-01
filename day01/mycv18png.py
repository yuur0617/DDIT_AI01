import cv2

frame = cv2.imread('k.jpg')

x = 100
y = 100
w = 100
h = 100

img = cv2.imread('mask/118.png', cv2.IMREAD_UNCHANGED)
resized_img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
alpha_channel = resized_img[:, :, 3] / 255.0

for c in range(0, 3):
    frame[y:y + h, x:x + w, c] = frame[y:y + h, x:x + w, c] * (1 - alpha_channel) + \
                                  resized_img[:, :, c] * alpha_channel



cv2.imshow('Lena color', frame)
 
cv2.waitKey(0)
cv2.destroyAllWindows()