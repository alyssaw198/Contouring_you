import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#eye_cascade2 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml') 

while True:
    ret, frame = cap.read() #Code that shows the webcame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Change the image to grayscale

    eyes = eye_cascade.detectMultiScale(gray, 1.05, 5)
    #eyes2 = eye_cascade2.detectMultiScale(gray, 1.05, 5)
    #faces = face_cascade.detectMultiScale(gray, 1.05, 6)
    for (ex, ey, ew, eh) in eyes:
        #print(ex,ey,ew,eh)
        cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

    '''
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.05, 5)
        eyes2 = eye_cascade2.detectMultiScale(roi_gray, 1.05, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)
        for (ex, ey, ew, eh) in eyes2:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)
    '''
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()