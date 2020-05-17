from picamera import PiCamera
from time import sleep

def showCamStream():
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.stop_preview()