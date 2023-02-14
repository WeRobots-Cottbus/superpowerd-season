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
    MotorTop.run_time(300,280)
    GyroDrive(150,300,gyro0+45)
    GyroDrive(-100,300,gyro0+45)
    GyroTurn(gyro0-45,30)
    GyroDrive(-150,150,gyro0-45,5)
    wait(500)
    GyroDrive(70,250,gyro0-45,5)
    
    GyroDrive(-80,150,gyro0-45,5)
    wait(500)
    GyroDrive(50,250,gyro0-45,5)
    
    GyroDrive(-80,150,gyro0-45,5)
    wait(500)
    GyroDrive(50,250,gyro0-45,5)

    GyroDrive(-80,150,gyro0-45,5)
    wait(500)
    GyroDrive(100,250,gyro0-25,6)

    GyroTurn(gyro0+45,30)
    GyroDrive(50,300,gyro0+45)


    MotorTop.run_time(300,430)
    wait(2000)
    GyroDrive(35,200,gyro0+45)
    MotorTop.run_time(-300,800)
    GyroDrive(-95,200,gyro0+45)
    MotorTop.run_time(500,600)
    GyroDrive(-90,200,gyro0+25,5)

    MotorTop.run_time(-600,700)
    MotorTop.run_time(600,500)

    GyroDrive(25,300,gyro0+33)
    MotorTop.run_time(-600,700)

    GyroDrive(90,300,gyro0+40)
    MotorTop.run_time(400,1000)

    GyroTurn(gyro0+35,30)
    GyroDrive(500,300,gyro0+20)

    MotorTop.run_time(-500,500,Stop.HOLD,False)
    MotorFront.run_angle(300,150)


    


if __name__ == "__main__":
    run()
