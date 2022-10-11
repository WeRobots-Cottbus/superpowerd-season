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
    Base.settings(350,350,150,150)
    Base.straight(350)
    Base.turn(50)
    Base.straight(365)
    Base.turn(-52)
    Base.straight(25)
    MotorTop.run_angle(250,600)
    MotorTop.run_angle(-250,600)
    MotorTop.run_angle(250,600)
    MotorTop.run_angle(-250,600)
    MotorTop.run_angle(250,600)
    MotorTop.run_angle(-350,600)
    Base.straight(300)

if __name__ == "__main__":
    run()
