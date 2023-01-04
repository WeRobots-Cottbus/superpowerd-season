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
def GyroDrive(distance:int, speed:float=200, gyro_start:int=Gyro.angle(),factor:int=3) -> None:
    
    
    if distance < 0:

        while Base.distance() >= distance:
            Base.drive(-speed,-((gyro_start-Gyro.angle())*factor))

    else:
        while Base.distance() <= distance:
            Base.drive(speed,-((gyro_start-Gyro.angle())*factor))


    Base.stop()
    Base.reset()
    print(gyro_start)

def GyroTurn(angle:int,speed:int):

    if angle > 0:
        while Gyro.angle() <= angle:
            print(Gyro.angle())
            Base.drive(-speed,-speed)

    elif angle < 0:
        while Gyro.angle() >= angle:
            print(Gyro.angle())
            Base.drive(speed,speed)

    Base.stop()
    Base.reset()
