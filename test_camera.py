from picamera import PiCamera
from time import sleep
#test change
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/mnt/public/image.jpg')
camera.stop_preview()