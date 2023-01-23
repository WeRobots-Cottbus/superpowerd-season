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
    GyroDrive(-260,350,gyro0)#erste geradeaus
    GyroDrive(-530,200,gyro0+45,1.5)
    GyroTurn(gyro0-45,30)
    GyroDrive(-150,150,gyro0-45,5)
    wait(500)
    GyroDrive(50,250,gyro0-45,5)
    
    GyroDrive(-80,150,gyro0-45,5)
    wait(500)
    GyroDrive(50,250,gyro0-45,5)
    
    GyroDrive(-80,150,gyro0-45,5)
    wait(500)
    GyroDrive(50,250,gyro0-45,5)

    GyroDrive(-80,150,gyro0-45,5)
    wait(500)
    GyroDrive(100,250,gyro0-15,6)

    GyroTurn(gyro0+45,30)
    GyroDrive(50,300,gyro0+45)

    MotorTop.run_time(500,500)
    GyroDrive(-100,200,gyro0+45)
    GyroTurn(gyro0+30,30)


    





    


if __name__ == "__main__":
    run()
