# -*- coding: utf-8 -*-
#!//usr/bin/python3
#Project mk11 developmed by weblima rafael_weblima@hotmail.com

from move import MoveCar
from feel import UltrasonicSensor
import time

move = MoveCar()
move.setDirection("stop")
move.setVelocity(0)

#starting ultrasonic sensor
distance = UltrasonicSensor(22, 32)
distance.setSleep(1)

try:
    while True:

        #print(distance.getDistance())

        #if distance.getDistance() > 10:
        #    m.setDirection("forward")
        #    m.setVelocity(60)
        #    m.toMove()
        #else:
        #    m.toStop(1)
        #    m.setDirection("rigth")
        #    m.setVelocity(60)
        #    m.toMove()

        move.toStop()
        time.sleep(2)

        move.setDirection("forward")
        move.setVelocity(60)
        move.toMove()
        time.sleep(2)

        move.toStop()
        time.sleep(2)

        move.setDirection("back")
        move.setVelocity(60)
        move.toMove()
        time.sleep(2)

        move.toStop()
        time.sleep(2)

        move.setDirection("left")
        move.setVelocity(60)
        move.toMove()
        time.sleep(2)

        move.toStop()
        time.sleep(2)

        move.setDirection("rigth")
        move.setVelocity(60)
        move.toMove()
        time.sleep(2)

except KeyboardInterrupt:
    print("finish script")
    move.toStop()
    exit()
finally:
    del move
    del distance






