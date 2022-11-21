#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys, os
sys.path.insert(0, "/home/robot/superpowerd-season")

from botconfig import *
from toolkit import *

PrgName = __file__.split("/")[-1][:-3]

"""
    Gyro.reset_angle(0)
    Base.settings(300,300,100,100)
    Base.straight(-250)
    
    while Gyro.angle() != -45:
        print(Gyro.angle())
        Base.drive(-20,50)
    print(Gyro.angle()) 


    Base.reset()
    while Base.distance() != -395:
        print(Base.distance())
        Base.drive(-200,0)
    Base.stop()
    MotorLeft.brake()
    MotorRight.brake()
    print(Gyro.angle())
    while Gyro.angle() != 0:
        print(Gyro.angle())
        Base.drive(-20,-50)
    print(Gyro.angle()) 
    Base.straight(-200)
    for _ in range(3):
        MotorTop.run_angle(-500,-400)
        MotorTop.run_angle(500,-400)
    MotorTop.run_time(-500,1000)
    Base.drive(250,25)

"""

def run():
    Gyro.reset_angle(0)
    Base.settings(300,300,100,100)
    Base.straight(-260)
    while Gyro.angle() >= -43:
        print(Gyro.angle())
        Base.drive(-30,30)
    print(Gyro.angle()) 
    Base.stop()
    MotorLeft.hold()   
    MotorRight.hold()
    Base.reset()
    
    while Base.distance() >= -320:
        Base.drive(-100,0)
    Base.stop()
    MotorLeft.hold()   
    MotorRight.hold()
    print(" Turn point after first turn: -----" + str(Gyro.angle()))
    
    Base.reset()
    while Gyro.angle() <= 0:
        print(Gyro.angle())
        Base.drive(-30,-30)
    print(Gyro.angle()) 
    
    Base.straight(-20)
    for _ in range(3):
        MotorTop.run_angle(-500,-500)
        MotorTop.run_angle(500,-500)
    MotorTop.run_time(-500,1000)
    Base.straight(500)
    Base.drive(250,70)
    
if __name__ == "__main__":
    run()
