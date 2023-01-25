#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from botconfig import *
from toolkit import *
from programs import prg1_1, prg2_1, prg3_1, prg4_1, prg5_1

#prg1_1 - Schwarzer ausfahrbahrer Arm
#prg2_1 - Roter Schiebe mechanismus beim solarfeld

prg_lst = [prg1_1, prg2_1, prg3_1,prg4_1,prg5_1]
prg_len = len(prg_lst)

prg_prev = lambda x: (x - 1) % prg_len
prg_next = lambda x: (x + 1) % prg_len

def loop():
    prg5_1.run()# tenp
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

def color_selection():
    while True:
        color = Colordetect.color()
        print(color)
        wait(100)
        if color == Color.BLUE: color=None
        if Button.CENTER in Brick.buttons.pressed():

            if color is not None:
                if color is Color.BLACK:
                    print("Schwarz")
                    prg1_1.run()
                elif color is Color.YELLOW:
                    print("Gelb")
                    prg2_1.run()
                elif color is Color.WHITE:
                    print("Weiß")
                    prg3_1.run()
                elif color is Color.RED:
                    print("Rot")
                    prg4_1.run()
                elif color is Color.GREEN:
                    print("Grün")
            else:
                DisplayText("Keine Farbe erkannt",(0,6))
                wait(500)

if __name__ == "__main__":
    prg4_1.run()
    #color_selection()


