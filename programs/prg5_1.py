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
    #program
    GyroDrive(550,300,gyro0,5)#fahrt richtung power to x
    GyroTurn(gyro0-45,40)#drehung ruchtung power to x
    GyroDrive(150,300,gyro0-45,5)#direkt zu power to x
    MotorFront.run_time(-400,500)#gabel runter
    GyroDrive(-70,300,gyro0-45)#kurz zurück um sie abzulegen
    GyroTurn(gyro0,40)#drehung richtung wasserresavoir
    GyroDrive(215,300,gyro0,5)#fahrt richtung wasserresavoir
    GyroTurn(gyro0-45,40)#drehung auf wasserresavoir
    GyroDrive(250,100,gyro0-45,1)#direkt auf wassereasavoir
    MotorTop.run_angle(180,180,Stop.HOLD,False)#einhaite rolle zur base
    GyroDrive(250,150,gyro0-43,0.5)#noch weiter gegenfahren


if __name__ == "__main__":
    run()
