#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from botconfig import *
from toolkit import *

mtr_lst = [(MotorTop, MotorFront), (MotorLeft, MotorRight)]
mtr_len = len(mtr_lst)

def loop():
    speed = 300
    mtr_sel = 0
    while True:
        # select motors
        if Button.CENTER in Brick.buttons.pressed(): mtr_sel = not mtr_sel
        
        # run or stop motors
        elif Button.UP    in Brick.buttons.pressed(): mtr_lst[mtr_sel][0].run(+speed)
        elif Button.DOWN  in Brick.buttons.pressed(): mtr_lst[mtr_sel][0].run(-speed)
        elif Button.LEFT  in Brick.buttons.pressed(): mtr_lst[mtr_sel][1].run(-speed)
        elif Button.RIGHT in Brick.buttons.pressed(): mtr_lst[mtr_sel][1].run(+speed)
        else:
            mtr_lst[mtr_sel][0].stop()
            mtr_lst[mtr_sel][1].stop()            

        # update display if center button is pressed
        if Button.CENTER in Brick.buttons.pressed():
            if mtr_sel:
                DisplayText("/\  MotorTop  \/", (4,2), True)
                DisplayText("<- MotorFront ->", (6,2))
            else:
                DisplayText("/\ MotorLeft  \/", (4,2), True)
                DisplayText("<- MotorRight ->", (6,2))
        
        # ui delay
        wait(250)

if __name__ == "__main__":
    loop()
