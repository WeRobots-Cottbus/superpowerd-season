#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys, os
sys.path.insert(0, "/home/robot/src_cc-os")

from botconfig import *
from toolkit import *

PrgName = __file__.split("/")[-1][:-3]

def run():
    Base.settings(300,300,150,150)
    Gyro.reset_angle(0)
    Base.straight(490) # erstes mal nach vorne
    print(Gyro.angle())
    Base.straight(-150)
    while Gyro.angle() <= 45:
        print(Gyro.angle())
        Base.drive(70,-70)
    Base.stop()
    Base.straight(515) # jedes mal anders ahhhhhhhhhhhhh
    while Gyro.angle() <= 90:
        print(Gyro.angle())
        Base.drive(100,-100) 
    Base.stop()
    Base.straight(150)
    MotorTop.run_angle(300,230)
    Base.straight(200)
    #dürfte klppen
    
    MotorTop.run_angle(300,-250)

    while Gyro.angle() != 90:
        if Gyro.angle() > 90:
            Base.drive(20,20)
        else:
            Base.drive(20,-20)
    Base.stop()

    #hand - klasppt noch nicht so gut
    Base.straight(230)
    MotorTop.run_angle(300,390)
    MotorTop.run_angle(200,-550)
    wait(500)
    Base.straight(200)
    MotorFront.run_angle(300,360)
    #solarfeld - noch weiter raus fahren
    MotorTop.run_angle(500,850)
    wait(10000)
    while Gyro.angle() != 90:
        if Gyro.angle() > 90:
            Base.drive(20,20)
        else:
            Base.drive(20,-20)
    Base.stop()

    Base.straight(300)



if __name__ == "__main__":
    run()
