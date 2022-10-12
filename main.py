#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from botconfig import *
from toolkit import *
from programs import prg1_1, prg2_1, prg3_1

prg_lst = [prg1_1, prg2_1, prg3_1]
prg_len = len(prg_lst)

prg_prev = lambda x: (x - 1) % prg_len
prg_next = lambda x: (x + 1) % prg_len

def loop():
    prg1_1.run() # tenp
    prg_sel = 0
    DisplayText(prg_lst[prg_sel].PrgName, (0,4),True)
    while True:
        # select program
        if   Button.LEFT   in Brick.buttons.pressed(): prg_sel = prg_prev(prg_sel)
        elif Button.RIGHT  in Brick.buttons.pressed(): prg_sel = prg_next(prg_sel)

        # run program
        elif Button.CENTER in Brick.buttons.pressed():
            DisplayText("is running", (0,6))
            prg_lst[prg_sel].run()
            DisplayText("", (0,6))

        # update display if any button is pressed
        if any(Brick.buttons.pressed()):
            DisplayText(prg_lst[prg_sel].PrgName, (0,4),True)

        # ui delay
        wait(250)

if __name__ == "__main__":
    loop()
