# -*- coding: utf-8 -*-
#!//usr/bin/python3
#Project mk11 developmed by rplima

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class UltrasonicSensor:

    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo

    def setSleep(self, sleep):
        self.sleep = sleep

    def getSleep(self, sleep):
        return self.sleep

    def getDistance(self):
        
        GPIO.setup(self.trig,GPIO.OUT)
        GPIO.setup(self.echo,GPIO.IN)

        GPIO.output(self.trig, False)
        time.sleep(self.sleep)

        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        while GPIO.input(self.echo)==0:
          pulse_start = time.time()

        while GPIO.input(self.echo)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        return distance
