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
    GyroDrive(-400,250,gyro0)#an die wand kacheln
    GyroDrive(19,250,gyro0)
    GyroTurn(gyro0+130,70)
    GyroTurn(gyro0+135,15)#drehung richtung windrad
    
    GyroDrive(200,250,gyro0+135,10)#ran
    wait(350)
    GyroDrive(-90,250,gyro0+135,5)#zurück
    
    GyroDrive(120,250,gyro0+135,10)#ran
    wait(350)
    GyroDrive(-90,250,gyro0+135,5)#zurück

    GyroDrive(120,250,gyro0+135,10)#ran
    wait(350)
    GyroDrive(-55,200,gyro0+135,5)#zurück
    
    GyroTurn(gyro0-40,70)#drehung mit einheiten zum trichter
    GyroTurn(gyro0-56,15)#end drehung genauer
    GyroDrive(130,150,gyro0-55)
    GyroTurn(gyro0-20,20)
    wait(1000)
    MotorFront.run_angle(300,400)#behäter hoch damit einhaiten liegen
    GyroDrive(-50,150,gyro0-10)#zurück
    GyroTurn(gyro0+43,30)#drehung zum auto
    GyroDrive(40,150,gyro0+44)#zurüc damit stange runter geht
    MotorTop.run_time(-1500,500)#runter stange
    GyroDrive(-30,150,gyro0+44)#vor 
    MotorTop.run_time(1500,1500)#stange hoch
    MotorTop.run_time(-1500,500)#stange runter
    GyroDrive(300,400,gyro0+40)#zurück in die base
    MotorTop.run_time(1500,1000)
    GyroDrive(800,400,gyro0+30)
    





    


if __name__ == "__main__":
    run()
