import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np

image = cv2.imread('002.jpg', cv2.IMREAD_COLOR) #이미지 불러오기
image = cv2.resize(image, (622, 504)) #resize

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

img_pillow = Image.fromarray(image)  # cv2 이미지를 Pillow 이미지로 변환

fontpath = "fonts/gulim.ttc" #폰트 
font = ImageFont.truetype(fontpath, 12) #글자 사이즈

b, g, r, a = 0, 255, 0, 255 #폰트 색상

# Pillow 이미지에 텍스트 그리기
draw = ImageDraw.Draw(img_pillow)
for (x, y, w, h) in faces:
    draw.rectangle([x, y, x + 65, y + 65], outline=(0, 255, 0), width=2)
    draw.text((x, y-20), "우민규 멍청이", font=font, fill=(b, g, r, a))

image_with_text = np.array(img_pillow)  # Pillow 이미지를 cv2 이미지로 변환

cv2.imshow('Face Detection', image_with_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
