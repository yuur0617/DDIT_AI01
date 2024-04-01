import cv2

cap = cv2.VideoCapture('img/김민경.mp4')

cnt = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        cv2.imwrite('pre01/{}.png'.format(cnt), frame)
        cnt += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()