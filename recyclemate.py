from gpiozero import LED
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

camera = PiCamera()
green_led = LED(17)
pir = MotionSensor(4)
green_led.off()

while True:
    pir.wait_for_motion()
    green_led.on()
    print("Motion Detected")
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    pir.wait_for_no_motion()
    green_led.off()
    print("Motion Stopped")