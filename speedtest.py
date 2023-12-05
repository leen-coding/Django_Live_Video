
from socket import *
import cv2
import numpy as np
from PIL import ImageGrab
import tkinter as tk

host = "127.0.0.1"


def select_area():
    def on_click(event):
        coords.append((event.x_root, event.y_root))
        if len(coords) == 2:
            # 两次点击后关闭窗口
            root.quit()

    root = tk.Tk()
    root.wait_visibility(root)
    root.attributes('-alpha', 0.3)  # 设置窗口透明度
    root.attributes('-fullscreen', True)  # 全屏

    coords = []
    root.bind('<Button-1>', on_click)  # 绑定鼠标点击事件

    root.mainloop()
    root.destroy()

    if len(coords) == 2:
        return (coords[0][0], coords[0][1], coords[1][0], coords[1][1])


def screenshot_area(coords):
    x1, y1, x2, y2 = coords
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    return np.array(img)


if __name__== "__main__":

    
    port = 5005
    Udp_Socket = socket(AF_INET,SOCK_DGRAM)
    coords = select_area()
    last_image = None
    while True:
        image = screenshot_area(coords)

        if last_image is not None:
            if np.array_equal(image, last_image):
                continue
        
        last_image = image

        image = cv2.resize(image, (400, 300))

        ret, jpeg = cv2.imencode('.jpg', image)
        frame_b = jpeg.tobytes()
        Udp_Socket.sendto(frame_b, (host, port))
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            Udp_Socket.close()

            break


