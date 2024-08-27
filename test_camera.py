from picamera import Pi 
from time import sleep

camera = Picamera()
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()