import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np

img = cv2.imread('dong.jpg', cv2.IMREAD_COLOR)
img_pillow = Image.fromarray(img) #cv2이미지를 pilow이미지로 변환

fontpath = "fonts/gulim.ttc"
font = ImageFont.truetype(fontpath, 24)

b,g,r,a = 0,0,255,255

draw = ImageDraw.Draw(img_pillow, 'RGBA')
draw.text((10, 10), "진실의 방으로 -", font=font, fill=(b,g,r,a))

img_draw = np.array(img_pillow) #pilow이미지를 cv2이미지로 변환

cv2.imshow('dong', img_draw) 

cv2.waitKey(0)
cv2.destroyAllWindows()