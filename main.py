#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Button, Color
from pybricks.tools import wait

from botconfig import *
from toolkit import *
from programs import prg1_1, prg2_1, prg3_1, prg4_1


PRG_LST = [prg1_1, prg2_1, prg3_1, prg4_1]
PRG_LEN = len(PRG_LST)

PRG_PREV = lambda x: (x - 1) % PRG_LEN
PRG_NEXT = lambda x: (x + 1) % PRG_LEN


def button_selection():
    global PRG_LST

    prg_sel = 0
    DisplayText(PRG_LST[prg_sel].PrgName, (0,4),True)
    while True:
        # select program
        if   Button.LEFT  in Brick.buttons.pressed(): prg_sel = PRG_PREV(prg_sel)
        elif Button.RIGHT in Brick.buttons.pressed(): prg_sel = PRG_NEXT(prg_sel)

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
    programs = {
        Color.BLACK:  (prg1_1, "Schwarz -> Gelb"),
        Color.YELLOW: (prg2_1, "Gelb -> Weiß"),
        Color.WHITE:  (prg3_1, "Weiß -> Rot"),
        Color.RED:    (prg4_1, "Rot")
    }

    while True:
        color = ColorDetect.color()
        wait(100)

        if Button.CENTER in Brick.buttons.pressed():
            color = ColorDetect.color()

            if programs.get(color):
                prg, msg = programs[color]
                print_message(msg)
                Brick.light.on(Color.RED)
                Brick.speaker.beep(500, 100)
                prg.run()
            else:
                print_message("Keine Farbe erkannt", is_error=True)


if __name__ == "__main__":
    Brick.speaker.beep(600, 250)
    color_selection()
    Brick.speaker.beep(100, 1_000)
    wait(1_000)
