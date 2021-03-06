
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

LED_PIN = 18

GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, True)
        time.sleep(1)
        GPIO.output(LED_PIN, False)
        time.sleep(1)
finally:
    GPIO.cleanup()

    
def buzzer():
    middle_c = 261
    p = GPIO.PWM(LED_PIN, middle_c)
    p.start(50)
    
    while True:
        for freq in range(200, 400, 10):
            p.ChangeFrequency(freq)
            time.sleep(0.1)
