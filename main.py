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
    Brick.color.off()
    while True:
        color = Colordetect.color()
        #DisplayText(str(color), (1,5))
        wait(100)

        if Button.CENTER in Brick.buttons.pressed():
            color = Colordetect.color()

            if color == Color.BLUE: 
                color=None
                DisplayText("Keine Farbe erkannt",(6,6))
                Brick.light.on(Color.RED)
                wait(200)
                Brick.light.off()
                wait(300)

            if color is not None:
                if color is Color.BLACK:
                    print("Schwarz")
                    DisplayText("Schwarz->Gelb",[2,6])
                    Brick.color.on(Color.Green)
                    prg1_1.run()
                    Brick.color.off()
                elif color is Color.YELLOW:
                    print("Gelb")
                    DisplayText("Gelb->Weiß",[2,6])
                    Brick.color.on(Color.Green)
                    prg2_1.run()
                    Brick.color.off()
                elif color is Color.WHITE:
                    print("Weiß")
                    DisplayText("Weiß->Rot",[2,6])
                    Brick.color.on(Color.Green)
                    prg3_1.run()
                    Brick.color.off()
                elif color is Color.RED:
                    print("Rot")
                    DisplayText("Rot",[2,6])
                    Brick.color.on(Color.Green)
                    prg4_1.run()
                    Brick.color.off()

if __name__ == "__main__":
    
    color_selection()


