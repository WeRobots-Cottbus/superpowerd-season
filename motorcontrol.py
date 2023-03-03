#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Button
from pybricks.tools import wait

from botconfig import *
from toolkit import *

MTR_LST = [(MotorTop, MotorForklift), (MotorLeft, MotorRight)]

def loop():
    global MTR_LST
    speed = 300
    mtr_sel = 0

    while True:
        # select motors
        if Button.CENTER in Brick.buttons.pressed(): mtr_sel = not mtr_sel
        
        # run or stop motors
        elif Button.UP    in Brick.buttons.pressed(): MTR_LST[mtr_sel][0].run(+speed)
        elif Button.DOWN  in Brick.buttons.pressed(): MTR_LST[mtr_sel][0].run(-speed)
        elif Button.LEFT  in Brick.buttons.pressed(): MTR_LST[mtr_sel][1].run(-speed)
        elif Button.RIGHT in Brick.buttons.pressed(): MTR_LST[mtr_sel][1].run(+speed)
        else:
            MTR_LST[mtr_sel][0].stop()
            MTR_LST[mtr_sel][1].stop()

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
