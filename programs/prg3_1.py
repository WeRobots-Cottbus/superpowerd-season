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
    Gyro.reset_angle(0)
    Base.settings(200,200,150,150)
        
    while Base.distance() <= 515:
        MotorTop.run_angle(3,3)
    Base.stop()
    
if __name__ == "__main__":
    run()
