#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys, os
sys.path.insert(0, "/home/robot/src_cc-os")

from botconfig import *
from toolkit import *

PrgName = __file__.split("/")[-1][:-3]

def run():
    Base.settings(300,300,250,250)
    Base.straight(280)
    Base.turn(45)
    Base.straight(325)
    Base.turn(-91)
    MotorTop.run_angle(-620,620)
    Base.straight(200)
    MotorTop.run_angle(620,620)
    Base.straight(90)
    MotorTop.run_angle(-620,620)
    Base.straight(-90)
    MotorTop.run_angle(620,620)
    Base.straight(80)
    MotorTop.run_angle(-620,620)
    Base.straight(-30)
    MotorTop.run_angle(620,330)
    Base.straight(-80)
    MotorTop.run_angle(-620,330)
    Base.straight(150)
    Base.turn(-60)
    Base.straight(-150)
    Base.turn(-120)
    Base.straight(1000)

if __name__ == "__main__":
    run()
