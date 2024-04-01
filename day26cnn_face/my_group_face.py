
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from day26cnn_face.my_pred_oop import AiFace
import cv2

af = AiFace()
image = cv2.imread('team.jpg')



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for idx,(x, y, w, h) in enumerate(faces):
    
    cropped_img = image[y: y + h, x: x + w]
    
    resize_img = cv2.resize(cropped_img, (32,32))
    myname = af.getNameByImage(resize_img)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    image = Image.fromarray(image) 
    draw = ImageDraw.Draw(image)
    font=ImageFont.truetype("fonts/gulim.ttc",20)
    draw.text((x,y-20),myname,font=font,fill=(255,255,0)) 
    image = np.array(image) 
    


    
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()