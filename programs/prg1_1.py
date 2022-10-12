#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys, os
sys.path.insert(0, "/home/robot/superpowerd-season")

from botconfig import *
from toolkit import *

PrgName = __file__.split("/")[-1][:-3]

def run():
    Base.settings(350,350,50,50)
    Base.straight(-250)
    Base.turn(60)
    Base.straight(-417)#small change
    Base.turn(-55)
    Base.straight(-250)
    MotorTop.run_angle(-200,-620)#bewgung zu groß
    MotorTop.run_angle(200,-620)

if __name__ == "__main__":
    run()
