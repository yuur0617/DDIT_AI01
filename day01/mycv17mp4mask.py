import cv2

cap = cv2.VideoCapture('sarang.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            
            img = cv2.imread('mask/118.png', cv2.IMREAD_UNCHANGED)
            resized_img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
            alpha_channel = resized_img[:, :, 3] / 255.0
            
            for c in range(0, 3):
                frame[y:y + h, x:x + w, c] = frame[y:y + h, x:x + w, c] * (1 - alpha_channel) + \
                                              resized_img[:, :, c] * alpha_channel
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            
   
        cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()