import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

up_arrow = 9
down_arrow = 10

GPIO.setup(up_arrow, GPIO.IN)
GPIO.setup(down_arrow, GPIO.IN)

num = 0
sleep_time = 0.2

while True:
    if GPIO.input(up_arrow):
        num = num + 1 if num < 255 else num
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    if GPIO.input(down_arrow):
        num = num - 1 if num > 0 else num
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    
    GPIO.output(leds, dec2bin(num))