#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys, os
sys.path.insert(0, "/home/robot/superpowerd-season")

from botconfig import MotorTop, MotorFront, MotorLeft, MotorRight, Gyro, ColorLeft, ColorRight, Base
from toolkit import GyroDrive

PrgName = __file__.split("/")[-1][:-3]
#working Haudrauf 2.0
def run():
    Gyro.reset_angle(0)
    gyro0 = Gyro.angle()
    Base.settings(50,50,50,50)

    MotorTop.run_angle(300, -100)
    GyroDrive(-500,300, gyro0)
    wait(500)
    GyroDrive(-200,100, gyro0)
    MotorTop.run_angle(400, -600)
    GyroDrive(800,400)


if __name__ == "__main__":
    run()
