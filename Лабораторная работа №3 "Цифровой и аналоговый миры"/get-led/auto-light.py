import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)

photo = 6
state = 0

GPIO.setup(photo, GPIO.IN)

while True:
    state = 1 - GPIO.input(photo)
    GPIO.output(led, state)
    time.sleep(0.2)
    state = 1