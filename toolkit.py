#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from math import pi

from botconfig import Brick, MotorForklift, MotorLeft, MotorRight, MotorTop, Gyro, ColorRight, ColorLeft, ColorDetect, Base
from botconfig import AxleTrack, WheelDiameter

"""coord[x,y]
+---------------------+
|0,0              21,0|
|                     |
|                     |
|                     |
|0,11            21,11|
+---------------------+"""
def DisplayText(text:str, coord:tuple[int,int]=(0,0), clear:bool=True, **kwargs) -> None:
    if clear: Brick.screen.clear()
    Brick.screen.draw_text(coord[0], coord[1], text, **kwargs)

"""       -77       0       +77
pivot:  ---|--------x--------|---   """
def TurnOnPivot(pivot:float, angle:float, speed:float, brake:bool=True) -> None:
    if angle == Gyro.angle(): return
    # calculate distance
    # formular: s = alpha/360° * 2pi * r
    distance_left = angle/360 * 2*pi * (AxleTrack/2 + pivot)
    distance_right = angle/360 * 2*pi * (AxleTrack/2 - pivot) 
    # correct distance, if pivot point is outside of the axle track
    if pivot < -AxleTrack/2:
        distance_left *= -1
    elif pivot > AxleTrack/2:
        distance_right *= -1
    # run until angle reached
    if Gyro.angle() < angle:
        while Gyro.angle() <= angle:
            MotorLeft.run(speed*abs(distance_left / distance_right))
            MotorRight.run(speed)
    else:
        while Gyro.angle() >= angle:
            MotorLeft.run(speed)
            MotorRight.run(speed*abs(distance_right / distance_left))
    # brake
    if brake:
        MotorLeft.hold()
        MotorRight.hold()
    else:
        MotorLeft.brake()
        MotorRight.brake()

#gyro geradeaus
#hier fahren wir geradeaus und checken dauerhaft wie unser gyro wert sich verändert
#wenn der wert sich in eine richtung(negativ oder postiv) verändert dann bewegen verändern wir unsere bewegung
#in die zu lösende richtung
def GyroDrive(distance:int, speed:float=200, gyro_start:int=0, factor:int=3, brake:bool=False) -> None:
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
def GyroTurn(angle:int, speed:int=20) -> None: 
    #drehung nach rechts
    if angle >= 0:
        while Gyro.angle() <= angle:#drehung solange bis gyro richtigen wert gibt
            print(Gyro.angle())
            Base.drive(-speed,-speed)#bewegung nach rechts

    #drehung nach links
    elif angle <= 0:
        while Gyro.angle() >= angle:#drehung solange bis gyro richtigen wert gibt
            print(Gyro.angle())
            Base.drive(speed,speed)#bewegun nach links

    Base.stop()#stop der Bewegung
    Base.reset()#reset der Bewegungen
