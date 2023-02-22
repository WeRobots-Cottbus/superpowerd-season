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
def text_wrap(text:str, length:int) -> str:
    out = []
    while text:
        out.append(text[:length])
        text = text[:length]
    return "\n".join(out)

def print_message(message:str):
    print(message)
    Brick.screen.clear()
    y_pos = 5
    for line in text_wrap(message, 25).split("\n"):
        Brick.screen.draw_text(2, y_pos, line)
        y_pos += 10

def wait_exit(ms:int=2_000):
    wait(ms)
    sys.exit()

print_error = lambda port, name: print_message("ERR Port {}: '{}'".format(port, name))

# Init Motors
try:
    MotorFront = Motor(Port.A)
except:
    print_error("A", "Motor Front")
    wait_exit()
try:
    MotorLeft = Motor(Port.B)
except:
    print_error("B", "Motor Left")
    wait_exit()
try:
    MotorRight = Motor(Port.C)
except:
    print_error("C", "Motor Right")
    wait_exit()
try:
    MotorTop = Motor(Port.D)
except:
    print_error("D", "Motor Top")
    wait_exit()

# Init Sensors
try:
    Gyro = GyroSensor(Port.S1)
except:
    print_error("1", "Gyro")
    wait_exit()
try:
    ColorRight = ColorSensor(Port.S2)
except:
    print_error("2", "Color Right")
    wait_exit()
try:
    ColorLeft  = ColorSensor(Port.S3)
except:
    print_error("3", "Color Left")
    wait_exit()
try:
    ColorDetect = ColorSensor(Port.S4)
except:
    print_error("4", "Color Detect")
    wait_exit()

# Init Base
try:
    Base = DriveBase(MotorLeft, MotorRight, 57, 154)
except:
    print_message("ERR Drivebase")
    wait_exit()
