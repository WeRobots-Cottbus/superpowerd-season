#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Port, Direction, Stop
from pybricks.ev3devices import ColorSensor, GyroSensor, Motor
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font

import sys
from math import pi

# config Base parameters
WheelDiameter = 57
AxleTrack = 154

# Init Brick
Brick = EV3Brick()
Brick.screen.set_font(Font("Consolas", 20, monospace=True))

# expand Motor class
class Motor(Motor):
    def __init__(self, port:Port, positive_direction:Direction=Direction.CLOCKWISE):
        self = super().__init__(port, positive_direction)
    # alias for run_angle
    def run_angel(self, speed:int, rotation_angle:int, then:Stop=Stop.HOLD, wait:bool=True):
        self.run_angle(speed, rotation_angle, then, wait)
    # run distance in mm
    def run_distance(self, speed:int, distance_mm:int, then:Stop=Stop.HOLD, wait:bool=True):
        global WheelDiameter
        self.run_angle(speed, distance_mm/(pi*WheelDiameter) * 360, then, wait)

# helper functions for catch init errors
def text_wrap(text:str, length:int) -> str:
    out = []
    while text:
        out.append(text[:length])
        text = text[length:]
    return "\n".join(out)

def print_message(message:str, max_length:int=25, is_error:bool=False):
    print(message)
    Brick.screen.clear()
    y_pos = 5
    for line in text_wrap(message, max_length).split("\n"):
        Brick.screen.draw_text(2, y_pos, line)
        y_pos += 20
    if is_error:
        Brick.light.on(Color.RED)
        Brick.speaker.beep(100, 500)
        wait(500)
        Brick.light.off()

def wait_exit(msec:int=4_000):
    wait(msec)
    sys.exit()

print_error = lambda port, name: print_message("[ERROR] Port {}: {}".format(port, name), is_error=True)

# Init Motors
try:
    MotorForklift = Motor(Port.A)
except Exception as error:
    print(error)
    print_error("A", "Motor Forklift")
    wait_exit()
try:
    MotorLeft = Motor(Port.B)
except Exception as error:
    print(error)
    print_error("B", "Motor Left")
    wait_exit()
try:
    MotorRight = Motor(Port.C)
except Exception as error:
    print(error)
    print_error("C", "Motor Right")
    wait_exit()
try:
    MotorTop = Motor(Port.D)
except Exception as error:
    print(error)
    print_error("D", "Motor Top")
    wait_exit()

# Init Sensors
try:
    Gyro = GyroSensor(Port.S1)
except Exception as error:
    print(error)
    print_error("1", "Gyro")
    wait_exit()
try:
    ColorRight = ColorSensor(Port.S2)
except Exception as error:
    print(error)
    print_error("2", "Color Right")
    wait_exit()
try:
    ColorLeft  = ColorSensor(Port.S3)
except Exception as error:
    print(error)
    print_error("3", "Color Left")
    wait_exit()
try:
    ColorDetect = ColorSensor(Port.S4)
except Exception as error:
    print(error)
    print_error("4", "Color Detect")
    wait_exit()

# Init Base
try:
    Base = DriveBase(MotorLeft, MotorRight, WheelDiameter, AxleTrack)
except Exception as error:
    print(error)
    print_message("[ERROR] Drivebase")
    wait_exit()
