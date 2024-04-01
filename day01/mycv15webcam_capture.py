import cv2

webcam = cv2.VideoCapture(0)

cnt = 0
while webcam.isOpened():
    status, frame = webcam.read()

    if status:
        cv2.imshow("test", frame)

    myKey = cv2.waitKey(1)
    if myKey == 97:
        cv2.imwrite("0{}.png".format(cnt), frame)
        cnt += 1
    if myKey == 113:
        break

webcam.release()
cv2.destroyAllWindows