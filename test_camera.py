from picamera import Picamera
from time import sleep
#test change
camera = Picamera()
camera.start_preview()
sleep(5)
camera.capture('/mnt/public/image.jpg')
camera.stop_preview()