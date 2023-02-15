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
from toolkit import GyroDrive, GyroTurn

PrgName = __file__.split("/")[-1][:-3]


def run():    
    #initilazing variables
    Gyro.reset_angle(0)
    gyro0 = Gyro.angle()
    #programm
    GyroDrive(450,300,gyro0)
    GyroTurn(gyro0+28,20)
    GyroDrive(515,350,gyro0+32)
    wait(500)
    GyroDrive(-140,250,gyro0)
    GyroTurn(gyro0+90,35)
    GyroTurn(gyro0+90,5)
    GyroDrive(-130,250,gyro0+90,5)
    GyroDrive(10,400,gyro0+90)
    GyroDrive(-10,400,gyro0+90)
    GyroDrive(15,400,gyro0+90)
    GyroTurn(gyro0-20,100)
    GyroDrive(700,400,gyro0-20)





    


if __name__ == "__main__":
    run()
