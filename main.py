from ultralytics import YOLO
import serial
import cv2
import pygame
import os
import time

pygame.init()
model = YOLO('yolov8n.pt')  # official weights are downloaded automatically on first run
# Serial port of the Arduino, e.g. COM7 on Windows or /dev/ttyACM0 on Linux.
ultrasonic_data = serial.Serial(os.getenv('SERIAL_PORT', 'COM7'), 9600)
cap = cv2.VideoCapture(0)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ret, frame = cap.read()
    z=model.predict(frame, show=True,classes=[0],verbose=False)
    x = ultrasonic_data.readline()
    val = str(x.decode().strip())
    dist = int(val)
    #This is the distance calculated using Ultrasonic sensor.
    d = 1000  # no person detected in this frame -> treat as out of range
    for i in z:
        boxes=i.boxes.numpy()
        if len(boxes)!=0:
            a,b,c,d=i.boxes.xyxy[0].tolist()
            x=int((a+c)/2)
            y=int((b+d)/2)
            w = c-a
            h = d-b
            W = 45
            f = 700
            d = (W*f)/w -10
    dist1 = int(d)
    # This is the distance calculated using camera
    if(dist>500 or dist1>500):
        print("No human in detection range....")
        cv2.rectangle(frame, (10, 10), (300, 50), (255, 255, 255), cv2.FILLED)
        cv2.putText(frame, "Detecting", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    elif(dist>200 and dist<=500 and dist1>200 and dist1<=500 ):
        print("Distance: ",dist)
        cv2.rectangle(frame, (10, 10), (300, 50), (255, 255, 255), cv2.FILLED)
        cv2.putText(frame, "Safe", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    elif(dist>100 and dist<=200 and dist1>100 and dist1<=200):
        print("Distance: ",dist," Close-> Inside layer 1")
        sound_file = 'warning.mp3'
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        time.sleep(1)
        cv2.rectangle(frame, (10, 10), (200, 50), (255, 255, 255), cv2.FILLED)
        cv2.putText(frame, "Close", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 210, 238), 3)
    elif(dist<=100 and dist1<100):
        print("Distance: ", dist, " Very Close-> Inside layer 2, Turn off machine")
        cv2.rectangle(frame, (10, 10), (300, 50), (255, 255, 255), cv2.FILLED)
        cv2.putText(frame, "Very Close", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        sound_file = 'alert.mp3'
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        time.sleep(1)
    cv2.imshow("image0.jpg", frame)

cap.release()
cv2.destroyAllWindows()
