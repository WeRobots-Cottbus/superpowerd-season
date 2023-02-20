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

    GyroDrive(None, None, 0, 4, True)#erste schnelle bewegung
    GyroDrive(None, None, 0, 4, True)#lagsam damit die einheit nicht weg fählt
    GyroDrive(-None, None, 0, 4, True)#zurück für die drehung auf rampe hin
    GyroTurn(55,30)#drehung auf rampe hin
    GyroDrive(None, None, 55, 4, True)#fahrt auf zur Rampe
    #entwerder jetzt schräg auf 90 grad oder einfache normal drehen
    GyroDrive(None, None, 90, 5, True)#fahrt bis kurz nach der Hand
    MotorTop.run_angle(None,None)#speed, angle raus um die einheite mit zu nehmen und die hand zulösen
    GyroDrive(None, None, 90, 7)#fahrt bis kurz richtung öl
    MotorTop.run_angle(None, None)#arm wieder rein damit wir nicht hängen beleiben
    
    GyroDrive(None,None,90,2)#an das öl fahren
    GyroDrive(-None,None,90,2)#weg vom öl fahren

    GyroDrive(None,None,90,2)#an das öl fahren
    GyroDrive(-None,None,90,2)#weg vom öl fahren

    GyroDrive(None,None,90,2)#an das öl fahren
    GyroDrive(-None,None,90,2)#weg vom öl fahren um sich drhen zu können

    GyroTurn(135,40)
    GyroDrive(None, None, 135, 5)#in die Base





if __name__ == "__main__":
    run()
