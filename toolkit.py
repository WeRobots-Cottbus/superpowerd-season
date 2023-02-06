#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from botconfig import *

"""
  for pixel placement       for text placement        for image placement
+---------------------+   +---------------------+   +---------------------+
|0,0             177,0|   |0,0              21,0|   |-177,-127    -177,127|
|                     |   |                     |   |                     |
|    Drawing Grid     |   |      Grid Array     |   |     Pixel Array     |
|                     |   |                     |   |                     |
|0,127         177,127|   |0,11            21,11|   |-177,127      177,127|
+---------------------+   +---------------------+   +---------------------+
"""
def DisplayText(text:str, coord:tuple[int,int]=(0,0), clear:bool=False, **kwargs) -> None:
    if clear: Brick.screen.clear()
    Brick.screen.draw_text(coord[0], coord[1], text, **kwargs)


GridArray_Debug = [
    ["0,0               21,0"],
    ["                      "],
    ["                      "],
    ["                      "],
    ["                      "],
    ["      Grid Array      "],
    ["  for text placement  "],
    ["                      "],
    ["                      "],
    ["                      "],
    ["                      "],
    ["0,11             21,11"]
]
GridArray_Box = [
    ["+--------------------+"],
    ["|                    |"],
    ["|                    |"],
    ["|                    |"],
    ["|                    |"],
    ["|                    |"],
    ["|                    |"],
    ["|                    |"],
    ["|                    |"],
    ["|                    |"],
    ["|                    |"],
    ["+--------------------+"]
]
def DisplayTextMatrix(text:list|str, clear:bool=False, **kwargs) -> None:
    if clear: Brick.screen.clear()
    if type(text) is str: text = text.split("\n")
    [ DisplayText(line, (i,0), False, **kwargs) for i, line in enumerate(text[:12]) ]


# gyro geradeaus
#hier fahren wir geradeaus und checken dauerhaft wie unser gyro wert sich verändert
#wenn der wert sich in eine richtung(negativ oder postiv) verändert dann bewegen verändern wir unsere bewegung
#in die zu lösende richtung
def GyroDrive(distance:int, speed:float=200, gyro_start:int=Gyro.angle(),factor:int=3) -> None:
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

#drehung mit bestimmtem drehmittelpunkt
#zum beispiel kann man sich auf den drehpunkt auf das rechte Rad setzen und dann dreht der roboter sich um das rechte rad
#pivot = drehpunkt
def TurnOnPivot(angle:int,speed:int,scale:int) -> None:
    #scale ist zwischen 0(links) - 100(rechts)
    #linke hälfte
    if scale < 50:
        if Gyro.angle() < angle:
            pass
    #rechte hälfte
    elif scale > 50:
        pass
    else:
        GyroTurn(angle,speed)
    turned = False

    