#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys, os
sys.path.insert(0, "/home/robot/superpowerd-season")

from botconfig import MotorTop, MotorFront, MotorLeft, MotorRight, Gyro, ColorRight, Base
from toolkit import GyroDrive, GyroTurn

PrgName = __file__.split("/")[-1][:-3]

#MotorTop = ausfahrbares dingsbums
#MotorFront = Gabelstapler

#Aufgaben: M08(20) | M05(20+10) | M04(20) | M02(15) | M09(Dino)

def run():
    
    #initilazing variables
    Gyro.reset_angle(0)
    gyro0 = Gyro.angle()

    GyroDrive(365,250,gyro0,4)#erste geradeaus
    wait(100)
    GyroDrive(105,150,gyro0+5,5)#langsamer wegen
    wait(500)
    GyroDrive(-113,200,gyro0)#zurück
    GyroTurn(gyro0+45,25)#drehung
    GyroDrive(455,250,gyro0+45,True)#danach geradeaus#temp###455
    wait(250)
    GyroTurn(gyro0+88,20)#drehen bei trichter
    #temp änderung
    GyroTurn(gyro0+90,5)
    GyroDrive(645,200,gyro0+92,True,4)#fahren zur hand
    wait(250)
    MotorTop.run_time(500,1200)#dingsbums raus
    wait(250)
    MotorTop.run_time(-800,1500)#dingsbums rein
    wait(500)
    GyroDrive(135,200,gyro0+92,True,4)#kurz geradeaus bis zum solarfeld
    MotorTop.run_angle(600,950)#raus zum solarfeld
    GyroDrive(420,150,gyro0+92,7)#geradeaus
    MotorTop.run_time(-450,1900)#dingsbums wieder rein
    GyroDrive(50,150,90,4)

    MotorFront.run_time(400,1600)#gabel hoch
    MotorFront.run_time(-400,900)#gabel runter
    
    MotorFront.run_time(400,1400)#gabel hoch
    MotorFront.run_time(-400,900)#gabel runter

    MotorFront.run_time(400,1600)#gabel hoch
        


    GyroDrive(-90,200,gyro0+90)#kurz wieder zurück
    Base.turn(-60)#drehung base
    GyroDrive(700,500,gyro0+90+60)#zur base


if __name__ == "__main__":
    run()
