#!//usr/bin/python3
#Project mk11 developmed by weblima rafael_weblima@hotmail.com

from interfaces import RpiGpioIntegration

#Sequence of pins conection betwean L298N and Raspibery Pi
#IN1=PIN7;IN2=PIN11;IN3=PIN13;IN4=PIN15

Hbi = RpiGpioIntegration(7, 11, 13, 15,) #Pins RPI
Hbi.setENA(4) #PCA9685 port 4
Hbi.setENB(5) #PCA9685 port 5
Hbi.pwmPCA9685(60) # Set frequency to 60hz

class MoveCar():

    def __init__(self):
        pass
    
    def setDirection(self, direction):
        self.direction = direction
    
    def setVelocity(self, velocity):
        self.velocity = velocity
    
    def getDirection(self):
        return self.direction
    
    def getVelocity(self):
        return self.velocity

    def toMove(self):

        if self.direction == "forward":
            print("moving forward")
            Hbi.dutyCycle(self.velocity)
            Hbi.setOutput(Hbi.getIN1(),False)
            Hbi.setOutput(Hbi.getIN2(),True)
            Hbi.setOutput(Hbi.getIN3(),True)
            Hbi.setOutput(Hbi.getIN4(),False)
        elif self.direction == "back":
            print("moving back")
            Hbi.dutyCycle(self.velocity)
            Hbi.setOutput(Hbi.getIN1(),True)
            Hbi.setOutput(Hbi.getIN2(),False)
            Hbi.setOutput(Hbi.getIN3(),False)
            Hbi.setOutput(Hbi.getIN4(),True)
        elif self.direction == "left":
            print("moving left")
            Hbi.dutyCycle(self.velocity)
            Hbi.setOutput(Hbi.getIN1(),True)
            Hbi.setOutput(Hbi.getIN2(),False)
            Hbi.setOutput(Hbi.getIN3(),True)
            Hbi.setOutput(Hbi.getIN4(),False)
        elif self.direction == "rigth":
            print("moving rigth")
            Hbi.dutyCycle(self.velocity)
            Hbi.setOutput(Hbi.getIN1(),False)
            Hbi.setOutput(Hbi.getIN2(),True)
            Hbi.setOutput(Hbi.getIN3(),False)
            Hbi.setOutput(Hbi.getIN4(),True)
    def toStop(self):
        print("stop")
        Hbi.dutyCycle(0)
        Hbi.setOutput(Hbi.getIN1(),False)
        Hbi.setOutput(Hbi.getIN2(),False)
        Hbi.setOutput(Hbi.getIN3(),False)
        Hbi.setOutput(Hbi.getIN4(),False)

class MoveUltrasonicSensor:
    def __init__(self):
        pass