#!//usr/bin/python3
#Project mk11 developmed by weblima rafael_weblima@hotmail.com

import RPi.GPIO as GPIO
import Adafruit_PCA9685

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class pca9685:
    def __init__(self):
        pass

    def getPWM(self):
        return self.PWM

    def setPWM(self, PWM):
        self.PWM = PWM

    def pwm(self, value):
        # Initialise the PCA9685 using the default address (0x40).
        pwm = Adafruit_PCA9685.PCA9685()
        # Set frequency to 60hz.
        pwm.set_pwm_freq(value)
        self.setPWM(pwm)

class Hbridge(pca9685):
    
    def __init__(self, IN1, IN2, IN3, IN4):
        super().__init__()

        self.IN1 = IN1
        self.IN2 = IN2
        self.IN3 = IN3
        self.IN4 = IN4

    def getIN1(self):
        return self.IN1
    
    def getIN2(self):
        return self.IN2

    def getIN3(self):
        return self.IN3

    def getIN4(self):
        return self.IN4

    def getENA(self):
        return self.ENA

    def getENB(self):
        return self.ENB

    def setIN1(self, IN1):
        self.IN1 = IN1
    
    def setIN2(self, IN2):
        self.IN2 = IN2
    
    def setIN3(self, IN3):
        self.IN3 = IN3
    
    def setIN4(self, IN4):
        self.IN4 = IN4
    
    def setENA(self, ENA):
        self.ENA = ENA
    
    def setENB(self, ENB):
        self.ENB = ENB
    
    #Private method declaration
    def __getPWMA(self): 
        return self.PWMA
    
    def __getPWMB(self):
        return self.PWMB

    def __setPWMA(self, PWMA):
        self.PWMA = PWMA
    
    def __setPWMB(self, PWMB):
        self.PWMB = PWMB

    #def __getPW(self):
    #    return self.PWM

    #def __setPWM(self, PWM):
    #    self.PWM = PWM
    #End of private methods
    
    def pwmRpi(self, value):
        #Method for control pwm for Raspibery Pi
        GPIO.setup(self.ENA,GPIO.OUT)
        GPIO.setup(self.ENB,GPIO.OUT)

        pwmA = GPIO.PWM(self.ENA, value)
        pwmA.start(0)
        self.__setPWMA(pwmA)

        pwmB = GPIO.PWM(self.ENB, value)
        pwmB.start(0)
        self.__setPWMB(pwmB)

    #def pwm(self, value):
    #    # Initialise the PCA9685 using the default address (0x40).
    #    pwm = Adafruit_PCA9685.PCA9685()
    #    # Set frequency to 60hz.
    #    pwm.set_pwm_freq(value)
    #    self.__setPWM(pwm)

    def setOutput(self, pin, state):
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,state)

    def dutyCycle(self, velocity):
        #Duty Cycle for Raspibery Pi
        a = self.__getPWMA()
        b = self.__getPWMB()
        
        a.ChangeDutyCycle(0)
        b.ChangeDutyCycle(0)
        a.ChangeDutyCycle(velocity)
        b.ChangeDutyCycle(velocity)

    def changeSpeed(self, speed):
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
        pwm.set_pwm(self.ENA, 0, pulseLeg)
        pwm.set_pwm(self.ENB, 0, pulseLeg)
    
    def cleanup(self):
        GPIO.cleanup()
    
    



