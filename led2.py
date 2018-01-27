import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)

PORT_L = 4
PORT_R = 17
GPIO.setup(PORT_L, GPIO.OUT)
GPIO.setup(PORT_R, GPIO.OUT)

while True:
    try:
        GPIO.output(PORT_L, GPIO.HIGH)
        GPIO.output(PORT_R, GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(PORT_L, GPIO.LOW)
        GPIO.output(PORT_R, GPIO.HIGH)
        time.sleep(0.3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
