#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys

Brick = EV3Brick()
def DisplayText(text:str, coord:tuple[int,int]=(0,0), clear:bool=True, **kwargs) -> None:
    if clear: Brick.screen.clear()
    Brick.screen.draw_text(coord[0], coord[1], text, **kwargs)
def print_message(message:str):
    print(message)
    DisplayText(message, (2,5))

#MOTOREN - Initialiesierend
try:    
    MotorFront = Motor(Port.A)
except:
    print_message("Motor-A ERROR")
    wait(2000)
    sys.exit()
try:
    MotorLeft = Motor(Port.B)
except:
    print_message("Motor-B ERROR")
    wait(2000)
    sys.exit()
try:
    MotorRight = Motor(Port.C)
except:
    print_message("Motor-C ERROR")
    wait(2000)
    sys.exit()
try:
    MotorTop = Motor(Port.D)
except:
    print_message("Motor-D ERROR")
    wait(2000)
    sys.exit()
try:
    Gyro= GyroSensor(Port.S1)
except:
    print_message("SENSOR-1 ERROR")
    wait(2000)
    sys.exit()
try:
    ColorRight = ColorSensor(Port.S2)#ColorSensor(Port.S2)
except:
    print_message("SENSOR-2 ERROR")
    wait(2000)
    sys.exit()
try:
    ColorLeft  = ColorSensor(Port.S3)
except:
    print_message("SENSOR-3 ERROR")
    wait(2000)
    sys.exit()
try:
    Colordetect = ColorSensor(Port.S4)
except:
    print_message("SENSOR-4 ERROR")
    wait(2000)
    sys.exit()


try:
    Base = DriveBase(MotorLeft, MotorRight, 57, 154)
except:
    print_message("DriveBase ERROR")
    wait(2000)
    sys.exit()