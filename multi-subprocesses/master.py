
import subprocess, sys
import time, keyboard

slaves = ["slave_1", "slave_2", "slave_3"]

def selector():
    global slaves
    ind = 0

    process = None
    while True:
        # check if the process has finished itself
        if process is not None and process.poll() is not None:
            process = None

        # check for left / right to switch selected slave
        if keyboard.is_pressed("left"):
            ind = (ind - 1) % 3
            print(f"{ind=}")
        elif keyboard.is_pressed("right"):
            ind = (ind + 1) % 3
            print(f"{ind=}")

        # if no slave is running, start slave as subprocess
        elif keyboard.is_pressed("enter"):
            if process is None:
                process = subprocess.Popen([sys.executable, f"./{slaves[ind]}.py"])
                print(f"subprocess started")
            else:
                print(f"another subprocess is running: {process}")

        # kill running subprocess
        elif keyboard.is_pressed("d"):
            if type(process) is subprocess.Popen:
                process.terminate()
                process = None
                print(f"subprocess killed")
            else:
                print(f"no subprocess is running")

        time.sleep(0.2)


if __name__ == "__main__":
    selector()
