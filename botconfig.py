#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


Brick = EV3Brick()
from toolkit import DisplayText
def print_message(message:str):
    print(message)
    DisplayText(message,[2,5])

#MOTOREN - Initialiesierend
try:    
    MotorFront = Motor(Port.A)
except:
    print_message("Motor-A ERROR")
try:
    MotorLeft = Motor(Port.B)
except:
    print_message("Motor-B ERROR")
try:
    MotorRight = Motor(Port.C)
except:
    print_message("Motor-C ERROR")
try:
    MotorTop = Motor(Port.D)
except:
    print_message("Motor-D ERROR")

try:
    Gyro= GyroSensor(Port.S1)
except:
    print_message("SENSOR-1 ERROR")
try:
    ColorRight = ColorSensor(Port.S2)#ColorSensor(Port.S2)
except:
    print_message("SENSOR-2 ERROR")
try:
    ColorLeft  = ColorSensor(Port.S3)
except:
    print_message("SENSOR-3 ERROR")
try:
    Colordetect = ColorSensor(Port.S4)
except:
    print_message("SENSOR-4 ERROR")


try:
    Base = DriveBase(MotorLeft, MotorRight, 57, 154)
except:
    print_message("DriveBase ERROR")