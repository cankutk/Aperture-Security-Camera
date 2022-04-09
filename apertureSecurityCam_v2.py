import cv2
import serial
import time
from datetime import datetime
from ayarlar import *

font = cv2.FONT_HERSHEY_SIMPLEX
yuz_tanima = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

kamera = cv2.VideoCapture(0)

kamera.set(3, 1280)
kamera.set(4, 720)

if arduino_durum == 1:
    arduino = serial.Serial(port, 9600, timeout=0.1)
    time.sleep(1)

while kamera.isOpened():
    ret, kare = kamera.read()
    if not ret:
        break

    tarih = datetime.now()
    zaman = tarih.strftime("%m/%d/%Y, %H:%M:%S")
    text = "Live Streaming"

    kare = cv2.flip(kare, 1)
    cv2.putText(kare, zaman, (850, 700), font, 1, (0, 0, 255), 2)
    cv2.putText(kare, "Aperture_Cam_01", (50, 700), font, 1, (255, 153, 0), 1)

    griYap = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    yuz = yuz_tanima.detectMultiScale(griYap, 1.1, 6)

    for x, y, w, h in yuz:

        konum = "X{0:d}Y{1:d}".format((x+w//2), (y+h//2))
        if arduino_durum == 1:
            arduino.write(konum.encode('utf-8'))
        print(konum)
        cv2.circle(kare, (x+w//2, y+h//2), 2, (204, 0, 0), 2)
        cv2.rectangle(kare, (x, y), (x+w, y+h), (255, 102, 153), 3)

    cv2.rectangle(kare, (610, 330),
                  (670, 390),
                  (153, 204, 255), 3)
    cv2.imshow("Aperture Security Camera", kare)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()
