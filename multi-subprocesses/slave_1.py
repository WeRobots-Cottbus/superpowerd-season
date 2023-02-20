
import time

def run():
    print(f"run slave 1")
    for i in range(20):
        print(f" slave 1: do step {i}")
        time.sleep(0.1)
    print(f"slave 1 finished")

if __name__ == "__main__":
    run()
