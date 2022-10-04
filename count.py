import cv2
import pickle
import numpy as np

counters = []

with open('lot.pkl', 'rb') as archive:
    counters = pickle.load(archive)

print(counters)

cap = cv2.VideoCapture('video.mp4')

while True:
    ret, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 27, 16)
    imgMd = cv2.medianBlur(imgTh, 5)
    kernel = np.ones((3, 3), np.int8)
    imgDil = cv2.dilate(imgMd, kernel)

    open = 0
    for x, y, w, h in counters:
        countDil = imgDil[y:y+h, x:x+w]
        #Calcula a quantidade de pixels brancos na imagem
        count = cv2.countNonZero(countDil)
        cv2.putText(img, str(count), (x,y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        if count < 900:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            open += 1
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.rectangle(img, (90,0), (415, 60), (0,255,0), -1)
        cv2.putText(img, f'LIVRE: {open}/69', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 5)

    cv2.imshow('Video', img)
    # cv2.imshow('Video Th', imgDil)
    cv2.waitKey(10)
