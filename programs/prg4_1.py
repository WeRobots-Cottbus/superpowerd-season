#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys
sys.path.insert(0, "/home/robot/superpowerd-season")

from botconfig import MotorTop, MotorFront, MotorLeft, MotorRight, Gyro, ColorLeft, ColorRight, Base
from toolkit import GyroDrive, GyroTurn

PrgName = __file__.split("/")[-1][:-3]


def run():
    #initilazing variables
    Gyro.reset_angle(0)
    gyro0 = Gyro.angle()
    #programm
    GyroDrive(-160,300,0,3,True)
    GyroDrive(-550,250,44,1.5,False)
    GyroDrive(-150,15,44,0.5)
    wait(200)
    GyroDrive(70,200,45,3,True)# weg vom auto
    MotorTop.run_time(-300,1000)#vorne anbauteil
    GyroDrive(20,300,45,3,True)
    GyroTurn(135,30)#drehung auf windrad
    wait(200)
    
    GyroDrive(250,250,139,6)#fahrt auf rad
    wait(600)
    GyroDrive(-40,200,135,6)

    GyroDrive(100,250,135,6)#fahrt auf rad
    wait(600)
    GyroDrive(-40,200,135,6)

    GyroDrive(100,250,135,6)#fahrt auf rad
    wait(600)
    GyroDrive(-250,200,180,3,True)
    GyroDrive(100,150,230,3,True)
    GyroTurn(290,40)
    GyroDrive(150,100,290,3,True)
    wait(500)
    #MotorFront.run_time(300,5000)

if __name__ == "__main__":
    run()
