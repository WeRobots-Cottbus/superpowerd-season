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

    GyroDrive(-220,300,gyro0)#erste geradeaus
    GyroTurn(gyro0-40,25)#drehung beim laster
    GyroDrive(-300,300,gyro0-40)#weiter richtung solarfeld
    GyroTurn(gyro0,20)#drehung auf box
    GyroDrive(-100,200,gyro0)#zu box hin
    GyroDrive(150,250)#zurück zum wasserdings
    GyroDrive(80,100,gyro0)#wasserdings auslösen
    GyroTurn(gyro0-45,30)#drehung in base 
    GyroDrive(350,300,gyro0-45)
print ("sofia ist unglaublich krass cool und hübsch und Tristan aber auch. Und Lego ist doof") 
    


if __name__ == "__main__":
    run()
