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

FACTOR = 10

def run():
    
    Gyro.reset_angle(0)
    gyro0 = Gyro.angle()
    Base.settings(300,300,150,150)
    GyroDrive(580,200,gyro0,FACTOR)#Fernsehr gegenfahren
    wait(1000)
    GyroDrive(-150,150,gyro0,FACTOR)#zurück
    GyroTurn(-45,50)


if __name__ == "__main__":
    run()
