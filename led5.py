import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)

ports = [5,6,13,19,26]
for i in ports:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

def led_on(no):
    for i, port in enumerate(ports):
        if no == i:
            v == GPIO.HIGH
        else:
            v = GPIO.LOW
        GPIO.output(port, v)
        
while True:
    try:
        for i in range(0, 5):
            led_on(i)
            time.sleep(0.1)
        for i in range (4, -1, -1):
            led_on(i)
            time.sleep(0.1)
        except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
