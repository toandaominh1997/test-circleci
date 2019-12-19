import numpy
import numpy as np 
from PIL import Image

from PyV4L2Camera.camera import Camera
from PyV4L2Camera.controls import ControlIDs

camera = Camera('/dev/video2', 1920, 1280)
controls = camera.get_controls()

for control in controls:
    print(control.name)

camera.set_control_value(ControlIDs.BRIGHTNESS, 48)
import cv2 
import time 

while(True):
    start = time.time()
    frame = camera.get_frame()
    # Decode the image
    pil_image = Image.frombytes('RGB', (camera.width, camera.height), frame, 'raw', 'RGB')
    img = cv2.cvtColor(numpy.asarray(pil_image), cv2.COLOR_RGB2BGR)
    cv2.imshow('Opencv', img)
    total_time = time.time() - start 
    print("FPS: {}".format(1/total_time))
    cv2.waitKey(1)

camera.close()
"""
sudo apt-get install libv4l-dev
pip install PyV4L2Camera
"""
