#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog

import sys
sys.path.insert(0, "/home/robot/superpowerd-season")

from botconfig import MotorForklift, MotorLeft, MotorRight, Gyro, ColorDetect, Base
from botconfig import MotorTop as MotorArm
from toolkit import GyroDrive, GyroTurn, TurnOnPivot

PrgName = __file__.split("/")[-1][:-3]

#Aufgaben: M08(20) | M05(20+10) | M04(20) | M02(15) | M09(Dino)

def run():
    
    #initilazing variables
    Gyro.reset_angle(0)
    gyro0 = Gyro.angle()

    GyroDrive(270, 300, 0, 4, True)#erste schnelle bewegung
    GyroDrive(100, 100, 0, 6, True)#langsam damit die einheit nicht weg fählt
    GyroDrive(-110, 200, 0, 4, True)#zurück für die drehung auf rampe hin
    GyroTurn(47, 20)#drehung auf rampe hin
    GyroDrive(550, 300, 47, 4, True)#fahrt auf zur Rampe
    #entwerder jetzt schräg auf 90 grad oder einfache normal drehen
    GyroDrive(100, 100, 70, 3, True)# magic auf 90 drehen
    GyroDrive(300, 300, 90, 2, True)# magic auf 90 drehen
    GyroTurn(88, 10)#drehung auf genau 90
    
    GyroDrive(350, 300, 88, 3, True)#fahrt bis kurz nach der Hand
    MotorArm.run_angle(400, 1_100)#speed, angle raus um die einheite mit zu nehmen und die hand zulösen
    GyroDrive(290, 300, 88, 3)#fahrt bis kurz richtung öl
    MotorArm.run_angle(400, -1_200)#speed, angle arm wieder rein

    GyroDrive(-10, 300, 90, 6, True)# öl auslösen
    GyroDrive(20, 300, 90, 2)
    GyroDrive(-10, 300, 90, 6, True)
    GyroDrive(20, 300, 90, 2)
    GyroDrive(-10, 300, 90, 6, True)
    GyroDrive(20, 300, 90, 2)
    GyroDrive(-40, 300, 90, 6, True) # kurz von öl weg

    GyroTurn(140, 100)
    GyroDrive(900, 400, 140, 5)#in die Base




if __name__ == "__main__":
    run()
