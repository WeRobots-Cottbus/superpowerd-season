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
    GyroDrive(-190,350,gyro0)#erste geradeaus
    GyroTurn(gyro0+45,50)#drehung in auto
    GyroDrive(-200,400,gyro0+45)#weiter zum auto
    GyroTurn(gyro0,50)
    GyroDrive(-400,400,gyro0)#an die wand kacheln
    GyroDrive(15,250,gyro0)
    GyroTurn(gyro0+130,40)
    GyroTurn(gyro0+135,15)#drehung richtung windrad
    
    GyroDrive(200,300,gyro0+135,10)#ran
    wait(250)
    GyroDrive(-120,250,gyro0+135,5)#zurück
    
    GyroDrive(150,250,gyro0+135,10)#ran
    wait(250)
    GyroDrive(-120,250,gyro0+135,5)#zurück

    GyroDrive(150,250,gyro0+135,10)#ran
    GyroDrive(-27,250,gyro0+135,5)#zurück
    wait(250)
    GyroTurn(gyro0-60,40)
    GyroDrive(90,150,gyro0-55)
    GyroTurn(gyro0-10,15)
    wait(1000)
    MotorFront.run_angle(400,300)
    GyroDrive(-50,150,gyro0-10)
    GyroTurn(gyro0+43,30)
    GyroDrive(40,150,gyro0+44)
    MotorTop.run_time(-1500,500)
    GyroDrive(-50,150,gyro0+44)
    MotorTop.run_time(1500,1500)
    MotorTop.run_time(-1500,500)
    GyroDrive(300,400,gyro0+40)
    MotorTop.run_time(1500,1000)
    GyroDrive(800,400,gyro0+30)
    





    


if __name__ == "__main__":
    run()
