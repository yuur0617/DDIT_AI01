import cv2

arr = [
    {'lbl':'0','f':'00','n':'김민경'},
    {'lbl':'1','f':'01','n':'김승연'},
    {'lbl':'2','f':'02','n':'김차은'},
    {'lbl':'3','f':'03','n':'김창용'},
    {'lbl':'4','f':'04','n':'김초희'},
    {'lbl':'5','f':'05','n':'김현우'},
    {'lbl':'6','f':'06','n':'남희수'},
    {'lbl':'7','f':'07','n':'박주호'},
    {'lbl':'8','f':'08','n':'박지원'},
    {'lbl':'9','f':'09','n':'배유림'},
    {'lbl':'10','f':'10','n':'백영웅'},
    {'lbl':'11','f':'11','n':'변상원'},
    {'lbl':'12','f':'12','n':'송은비'},
    {'lbl':'13','f':'13','n':'우민규'},
    {'lbl':'14','f':'14','n':'유길상'},
    {'lbl':'15','f':'15','n':'이미소'},
    {'lbl':'16','f':'16','n':'이상철'},
    {'lbl':'17','f':'17','n':'이성휘'},
    {'lbl':'18','f':'18','n':'정민지'},
    {'lbl':'19','f':'19','n':'하예종'}
]

def mp4Toimg(myname,folder_name):
    cap = cv2.VideoCapture('img/{}.mp4'.format(myname))
    cnt = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for idx,(x, y, w, h) in enumerate(faces):
                # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cropped_img = frame[y: y + h, x: x + w]
                # cv2.imshow('{}'.format(idx), cropped_img)
                cropped_img = cv2.resize(cropped_img, (32, 32))
                cv2.imwrite('pre01/{}/{}.png'.format(folder_name,cnt),cropped_img)
                cnt+=1
        else:
            break


for a  in arr:
    print(a['n'],a['f'])
    mp4Toimg(a['n'],a['f'])
    # mp4Toimg("김민경","00")
    # mp4Toimg("김승연","01")
    
    
    
    
    
    
    
    
    