import time
from socket import *
import cv2
host = "192.168.0.25"
port = 5005

Udp_Socket = socket(AF_INET,SOCK_DGRAM)
Udp_Socket.bind((host, 6543))
video = cv2.VideoCapture(0)
while True:


    success, image = video.read()
    image = cv2.resize(image, (400, 300))
    ret, jpeg = cv2.imencode('.jpg', image)
    frame_b = jpeg.tobytes()
    Udp_Socket.sendto(frame_b, (host, port))
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        Udp_Socket.close()
        video.release()
        break


