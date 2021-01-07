#!//usr/bin/python3
#Project mk11 developmed by weblima rafael_weblima@hotmail.com

import RPi.GPIO as GPIO
import Adafruit_PCA9685

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class PWMcontroller:
    def __init__(self):
        pass

    def getPWMA(self): 
        return self.PWMA
    
    def getPWMB(self):
        return self.PWMB

    def setPWMA(self, PWMA):
        self.PWMA = PWMA
    
    def setPWMB(self, PWMB):
        self.PWMB = PWMB

    def getPWM(self):
        return self.PWM

    def setPWM(self, PWM):
        self.PWM = PWM

    def pwmPCA9685(self, value):
        # Initialise the PCA9685 using the default address (0x40).
        pwm = Adafruit_PCA9685.PCA9685()
        # Set frequency to 60hz.
        pwm.set_pwm_freq(value)
        self.setPWM(pwm)
        
    def pwmRPI(self, value):
        #Method for control pwm for Raspibery Pi
        GPIO.setup(self.getENA(),GPIO.OUT)
        GPIO.setup(self.getENB(),GPIO.OUT)

        pwmA = GPIO.PWM(self.getENA(), value)
        pwmA.start(0)
        self.setPWMA(pwmA)

        pwmB = GPIO.PWM(self.getENB(), value)
        pwmB.start(0)
        self.setPWMB(pwmB)

class Hbridge(PWMcontroller):
    
    def __init__(self, IN1, IN2, IN3, IN4):
        super().__init__()

        self.__IN1 = IN1
        self.__IN2 = IN2
        self.__IN3 = IN3
        self.__IN4 = IN4

    def getIN1(self):
        return self.__IN1
    
    def getIN2(self):
        return self.__IN2

    def getIN3(self):
        return self.__IN3

    def getIN4(self):
        return self.__IN4

    def getENA(self):
        return self.__ENA

    def getENB(self):
        return self.__ENB

    def setENA(self, ENA):
        self.__ENA = ENA
    
    def setENB(self, ENB):
        self.__ENB = ENB
    
class RpiGpioIntegration(Hbridge):
    def __init__(self, IN1, IN2, IN3, IN4):
        super().__init__(IN1, IN2, IN3, IN4)

    def setOutput(self, pin, state):
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,state)

    def dutyCycleRpi(self, velocity):
        #Duty Cycle for Raspibery Pi
        a = self.getPWMA()
        b = self.getPWMB()
        
        a.ChangeDutyCycle(0)
        b.ChangeDutyCycle(0)
        a.ChangeDutyCycle(velocity)
        b.ChangeDutyCycle(velocity)

    def dutyCycle(self, speed):
        #Max pulse length out of 4096
        minPulse = 2460
        maxPulse = 4090 

        if speed == 0 or (speed >= 60  and speed <= 100):
            pulseLeg = maxPulse 
            pulseLeg *= speed
            pulseLeg //= 100
        else:
            pulseLeg = minPulse

        pwm = self.getPWM()
        pwm.set_pwm(self.getENA(), 0, pulseLeg)
        pwm.set_pwm(self.getENB(), 0, pulseLeg)

    def cleanup(self):
        GPIO.cleanup()
    
    



