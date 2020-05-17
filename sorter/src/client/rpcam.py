from picamera import PiCamera
from time import sleep
import matplotlib.pyplot as plt

def showCamStream():
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    
    
    plt.plot([-1, -4.5, 16, 23, 15, 59])
    plt.show()