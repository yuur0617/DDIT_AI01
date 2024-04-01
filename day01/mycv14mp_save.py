import cv2

cap = cv2.VideoCapture('sarang.mp4')

#재생할 파일의 넓이와 높이
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("재생할 파일 넓이, 높이 : %d, %d"%(width, height))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('junjang.mp4', fourcc, 30.0, (int(width), int(height)))

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == False:
        break;
    
    cv2.imshow('frame',frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()