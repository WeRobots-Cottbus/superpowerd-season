#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Button, Color
from pybricks.tools import wait

from botconfig import *
from toolkit import *
from programs import prg1_1, prg2_1, prg3_1, prg4_1, prg5_1


PRG_LST = [prg1_1, prg2_1, prg3_1,prg4_1,prg5_1]
PRG_LEN = len(PRG_LST)

PRG_PREV = lambda x: (x - 1) % PRG_LEN
PRG_NEXT = lambda x: (x + 1) % PRG_LEN

def button_selection():
    global PRG_LST

    prg_sel = 0
    DisplayText(PRG_LST[prg_sel].PrgName, (0,4),True)
    while True:
        # select program
        if   Button.LEFT   in Brick.buttons.pressed(): prg_sel = PRG_PREV(prg_sel)
        elif Button.RIGHT  in Brick.buttons.pressed(): prg_sel = PRG_NEXT(prg_sel)

        # run program
        elif Button.CENTER in Brick.buttons.pressed():
            DisplayText("is running", (0,6))
            PRG_LST[prg_sel].run()
            DisplayText("", (0,6))

        # update display if any button is pressed
        if any(Brick.buttons.pressed()):
            DisplayText(PRG_LST[prg_sel].PrgName, (0,4),True)

        # ui delay
        wait(250)

def color_selection():
    while True:
        color = ColorDetect.color()
        #DisplayText(str(color), (1,5))
        wait(100)

        if Button.CENTER in Brick.buttons.pressed():
            color = ColorDetect.color()

            if color == Color.BLUE: 
                color=None
                DisplayText("Keine Farbe erkannt",(6,6))
                Brick.light.on(Color.RED)
                wait(200)
                Brick.light.off()
                wait(300)

            if color is not None:
                if color is Color.BLACK:
                    print_message("Schwarz->Gelb")
                    Brick.light.on(Color.GREEN)
                    prg1_1.run()
                elif color is Color.YELLOW:
                    print_message("Gelb->Weiß")
                    Brick.light.on(Color.GREEN)
                    prg2_1.run()
                elif color is Color.WHITE:
                    print_message("Weiß->Rot")
                    Brick.light.on(Color.GREEN)
                    prg3_1.run()
                elif color is Color.RED:
                    print_message("Rot")
                    Brick.light.on(Color.GREEN)
                    prg4_1.run()
                
                Brick.light.off()

def color_selection_master():
    pass

if __name__ == "__main__":
    Brick.speaker.beep()
    color_selection()
    wait(1_000)
