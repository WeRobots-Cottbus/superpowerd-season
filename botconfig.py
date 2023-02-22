#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

import sys

# Init Brick
Brick = EV3Brick()

# helper functions for catch init errors
def print_message(message:str):
    print(message)
    Brick.screen.clear()
    Brick.screen.draw_text(2, 5, message)

def wait_exit(ms:int=2_000):
    wait(ms)
    sys.exit()

# Init Motors
try:
    MotorFront = Motor(Port.A)
except:
    print_message("[ERROR] Port A: 'Motor Front'")
    wait_exit()
try:
    MotorLeft = Motor(Port.B)
except:
    print_message("[ERROR] Port B: 'Motor Left'")
    wait_exit()
try:
    MotorRight = Motor(Port.C)
except:
    print_message("[ERROR] Port C: 'Motor Right'")
    wait_exit()
try:
    MotorTop = Motor(Port.D)
except:
    print_message("[ERROR] Port D: 'Motor Top'")
    wait_exit()

# Init Sensors
try:
    Gyro= GyroSensor(Port.S1)
except:
    print_message("[ERROR] Port 1: 'Gyro'")
    wait_exit()
try:
    ColorRight = ColorSensor(Port.S2)
except:
    print_message("[ERROR] Port 2: 'Color Right'")
    wait_exit()
try:
    ColorLeft  = ColorSensor(Port.S3)
except:
    print_message("[ERROR] Port 3: 'Color Left'")
    wait_exit()
try:
    Colordetect = ColorSensor(Port.S4)
except:
    print_message("[ERROR] Port 4: 'Color Detect'")
    wait_exit()

# Init Base
try:
    Base = DriveBase(MotorLeft, MotorRight, 57, 154)
except:
    print_message("[ERROR] Drivebase")
    wait_exit()
