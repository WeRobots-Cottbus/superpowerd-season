
import slave_1, slave_2, slave_3
import threading
# import _thread
import time, keyboard

slaves = [slave_1, slave_2, slave_3]

# stopable thread
class MyThread(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        super().__init__(target=target, args=args, kwargs=kwargs)
        self._stop_event = threading.Event()
    # kill thread
    def kill(self):
        self._stop_event.set()
    # check if thread is running
    def is_alive(self):
        return super().is_alive() and not self._stop_event.is_set()

def selector():
    global slaves
    ind = 0

    dead_thread = MyThread(target=lambda:())
    dead_thread.start()
    thread = dead_thread

    while True:

        # check for left / right to switch selected slave
        if keyboard.is_pressed("left"):
            ind = (ind - 1) % 3
            print(f"{ind=}")
        elif keyboard.is_pressed("right"):
            ind = (ind + 1) % 3
            print(f"{ind=}")
        
        # if no slave is running, start slave as thread
        elif keyboard.is_pressed("enter"):
            if not thread.is_alive():
                thread = MyThread(target=slaves[ind].run)
                thread.start()
                print(f"thread started")
            else:
                print(f"another thread is running: {thread}")
        
        # kill running thread
        elif keyboard.is_pressed("d"):
            print(thread)
            if thread.is_alive():
                thread.kill()
                print(f"thread killed")
            else:
                print(f"no thread is running")

        time.sleep(0.2)


if __name__ == "__main__":
    selector()
