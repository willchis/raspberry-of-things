
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

LED_PIN = 18

GPIO.setup(LED_PIN,GPIO.OUT)

while True:
    GPIO.output(LIGHT,True)
    time.sleep(1)
    GPIO.output(LIGHT,False)
    time.sleep(1)
    print("Hello World")
