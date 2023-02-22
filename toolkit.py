#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from math import pi

from botconfig import Brick, MotorFront, MotorLeft, MotorRight, MotorTop, Gyro, ColorRight, ColorLeft, ColorDetect, Base
from botconfig import AxleTrack, WheelDiameter

"""
+---------------------+
|0,0              21,0|
|                     |
|      Grid Array     |
|                     |
|0,11            21,11|
+---------------------+
"""
def DisplayText(text:str, coord:tuple[int,int]=(0,0), clear:bool=True, **kwargs) -> None:
    if clear: Brick.screen.clear()
    Brick.screen.draw_text(coord[0], coord[1], text, **kwargs)

# pivot:    |--------x--------|
#           -        0        +
def TurnOnPivot(pivot:float, relative_angle:float, speed:float, stop:Stop=Stop.HOLD) -> None:
    # calculate the distance and the corresponding angle
    # formular: s = alpha/360° * 2pi * r
    distance_left = relative_angle/360 * 2*pi * (pivot + AxleTrack/2)
    distance_right = relative_angle/360 * 2*pi * (AxleTrack/2 - pivot)
    # formular: gamma = s/U * 360 = s/(pi*d) * 360
    angle_left = distance_left/(pi*WheelDiameter) * 360
    angle_right = distance_right/(pi*WheelDiameter) * 360
    # run angle
    MotorLeft.run_angle(speed, angle_left, stop, False)
    MotorRight.run_angle(speed, -angle_right, stop, False)

#gyro geradeaus
#hier fahren wir geradeaus und checken dauerhaft wie unser gyro wert sich verändert
#wenn der wert sich in eine richtung(negativ oder postiv) verändert dann bewegen verändern wir unsere bewegung
#in die zu lösende richtung
def GyroDrive(distance:int, speed:float=200, gyro_start:int = 0, factor:int=3, brake:bool=False) -> None:
    Base.reset()

    #rückwärts Bewegung
    if distance < 0:

        while Base.distance() >= distance:#solange wir noch nicht die zufahrende distanz gefahren sind
            Base.drive(-speed,-((gyro_start-Gyro.angle())*factor))#berechnung des zu drehenden Faktors der und wieder zum ausgangswert bewegt

    #vorwärts Bewegung
    else:
        while Base.distance() <= distance:#solanfe wir noch nicht die zufahrende distanz gefrahren sind
            Base.drive(speed,-((gyro_start-Gyro.angle())*factor))#berechnung des zu drehenden Faktors der und wieder zum ausgangswert bewegt

    Base.stop()
    Base.reset()
    if brake:
        MotorLeft.hold()
        MotorRight.hold()
    print("Gestartet bei: "+ str(gyro_start) +"\n Geendet bei: " + str(Gyro.angle()))

#drehung auf einen gyrowert
#nutzung in userem Program nicht als jede drehung einzel sonder ein 0 wert wird gesetzt un darauf wird
#werden dann alle andere werte berchnet. So wird dreht sich der roboter bei 90 grad immer auf die gleichen 90 grad.
def GyroTurn(angle:int,speed:int=20) -> None: 
    turned = False

    #drehung nach rechts
    if angle >= 0 and turned is False:
        while Gyro.angle() <= angle:#drehung solange bis gyro richtigen wert gibt
            print(Gyro.angle())
            Base.drive(-speed,-speed)#bewegung nach rechts
        turned = True#changing turned value

    #drehung nach links
    if angle <= 0 and  turned is False:
        while Gyro.angle() >= angle:#drehung solange bis gyro richtigen wert gibt
            print(Gyro.angle())
            Base.drive(speed,speed)#bewegun nach links

    Base.stop()#stop der Bewegung
    Base.reset()#reset der Bewegungen
