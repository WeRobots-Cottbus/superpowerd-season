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

#MotorTop = ausfahrbares dingsbums
#MotorFront = Gabelstapler

def run():
    
    #initilazing variables
    Gyro.reset_angle(0)
    gyro0 = Gyro.angle()

    GyroDrive(350,250,gyro0,5)#erste geradeaus
    wait(100)
    GyroDrive(120,150,gyro0)#langsamer wegen
    wait(500)
    GyroDrive(-100,200,gyro0)#zurück
    GyroTurn(gyro0+45,30)#drehung
    GyroDrive(455,250,gyro0+45)#danach geradeaus#temp
    wait(250)
    GyroTurn(gyro0+88,20)#drehen bei trichter
    wait(500)
    #temp änderung
    GyroDrive(610,200,gyro0+90)#fahren zur hand
    wait(250)
    MotorTop.run_angle(500,600)#dingsbums raus
    wait(250)
    MotorTop.run_angle(-300,500)#dingsbums rein
    wait(500)
    GyroDrive(130,200,gyro0+90)#kurz geradeaus bis zum solarfeld
    MotorTop.run_angle(600,800)#raus zum solarfeld
    GyroDrive(500,150,gyro0+90,7)#geradeaus

    MotorFront.run_angle(400,525)#gabel hoch
    MotorFront.run_angle(-400,295)#gabel runter
    
    MotorFront.run_angle(400,295)#gabel hoch
    MotorFront.run_angle(-400,295)#gabel runter

    MotorFront.run_angle(400,295)#gabel hoch

    MotorTop.run_angle(-550,800)#dingsbums wieder rein

    GyroDrive(-90,200,gyro0+90)
    Base.turn(-60)
    GyroDrive(600,500,gyro0+90+60)


if __name__ == "__main__":
    run()
