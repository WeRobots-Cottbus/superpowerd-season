#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Button, Color
from pybricks.tools import wait

import subprocess, sys

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
    while True:
        color = ColorDetect.color()
        wait(100)

        if Button.CENTER in Brick.buttons.pressed():
            color = ColorDetect.color()

            if color is Color.BLACK:
                print_message("Schwarz -> Gelb")
                Brick.light.on(Color.GREEN)
                prg1_1.run()
            elif color is Color.YELLOW:
                print_message("Gelb -> Weiß")
                Brick.light.on(Color.GREEN)
                prg2_1.run()
            elif color is Color.WHITE:
                print_message("Weiß -> Rot")
                Brick.light.on(Color.GREEN)
                prg3_1.run()
            elif color is Color.RED:
                print_message("Rot")
                Brick.light.on(Color.GREEN)
                prg4_1.run()
            else:
                print_message("Keine Farbe erkannt", is_error=True)


def color_selection_master():
    programs = {
        Color.BLACK:  ("prg1_1", "Schwarz -> Gelb"),
        Color.YELLOW: ("prg2_1", "Gelb -> Weiß"),
        Color.WHITE:  ("prg3_1", "Weiß -> Rot"),
        Color.RED:    ("prg4_1", "Rot")
    }
    process = None

    while True:
        wait(100)

        if Button.CENTER in Brick.buttons.pressed():
            color = ColorDetect.color()

            if process is not None and process.poll() is not None:
                if programs.get(color):
                    name, msg = programs[color]
                    print_message(msg)
                    Brick.light.on(Color.RED)
                    Brick.speaker.beep(500, 100)
                    process = subprocess.Popen([
                        sys.executable,
                        "./programs/{}.py".format(name)
                    ])
                else:
                    print_message("Keine Farbe erkannt", is_error=True)   
            else:
                print_message("Ein anderes Programm läuft noch", is_error=True)
        
        else:
            if type(process) is subprocess.Popen:
                process.terminate()
                process = None
                print_message("Programm beendet")
            else:
                print_message("Es läuft kein Programm")


if __name__ == "__main__":
    Brick.speaker.beep(600, 250)
    color_selection_master()
    wait(1_000)
