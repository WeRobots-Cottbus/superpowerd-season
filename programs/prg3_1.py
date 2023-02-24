#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog

import sys
sys.path.insert(0, "/home/robot/superpowerd-season")

from botconfig import MotorForklift, MotorTop, MotorLeft, MotorRight, Gyro, ColorDetect, Base
from toolkit import GyroDrive, GyroTurn, TurnOnPivot

PrgName = __file__.split("/")[-1][:-3]


def run():    
    #initilazing variables
    Gyro.reset_angle(0)
    gyro0 = Gyro.angle()
    #programm
    GyroDrive(65,300,0,3)
    GyroDrive(530,250,90,0.6)
    GyroDrive(80,100,90,4,True)
    wait(250)
    GyroDrive(-150,100,90,2,True)#sachen stehen lassen

    GyroTurn(10,30)#drehung auf trichter
    GyroDrive(400,500,10)#auf den trichter fahren
    GyroTurn(45,50)
    GyroDrive(90,200,45,3)
    GyroDrive(-150,200,0,1,True)
    GyroTurn(88,70)

    GyroDrive(-30,200,90,3)
    GyroDrive(30,300,90,3,True)

    GyroDrive(-30,200,90,3)
    GyroDrive(50,300,90,4,True)
    GyroTurn(-45,200)#drehung richtung base osten
    GyroDrive(300,300,-45)
    GyroDrive(600,300,0,5)


if __name__ == "__main__":
    run()
