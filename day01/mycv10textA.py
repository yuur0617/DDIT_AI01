# import cv2
#
# img = cv2.imread('dong.jpg', cv2.IMREAD_COLOR)
#
# img = cv2.putText(img, "마동석", (300, 150), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 1, cv2.LINE_AA)
#
# cv2.imshow('dong', img) 
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#===============================================================================

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

image = cv2.imread('dong.jpg')

image = Image.fromarray(image) #img배열을 PIL이 처리가능하게 변환

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("fonts/gulim.ttc",40)
draw.text((300,100),"마동석",font=font,fill=(255,0,255)) #text를 출력
image = np.array(image) #다시 OpenCV가 처리가능하게 np 배열로 변환

cv2.imshow("A",image)
cv2.waitKey()
cv2.destroyAllWindows()
