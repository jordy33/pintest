import RPi.GPIO as GPIO
import time
ports=[2,3,4,17,27,22,10,9,11,5,6,13,19,26,18,23,24,25,8,7,12,16,20,21]

GPIO.setmode (GPIO.BCM)
for item in ports:
    GPIO.setup (item,GPIO.OUT)
    GPIO.output (item,0)
while True:    
    for item in ports:
        GPIO.setup (item,GPIO.OUT)
        GPIO.output (item,1)
        time.sleep(.5)
        GPIO.output (item,0)