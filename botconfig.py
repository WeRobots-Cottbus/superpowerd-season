#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

Brick = EV3Brick()

MotorTop   = Motor(Port.A)
MotorLeft  = Motor(Port.B)
MotorRight = Motor(Port.C)
MotorFront = Motor(Port.D)

Gyro       = GyroSensor( Port.S1)
ColorLeft  = ColorSensor(Port.S3)
ColorRight = ColorSensor(Port.S4)

Base = DriveBase(MotorLeft, MotorRight, 57, 154)
