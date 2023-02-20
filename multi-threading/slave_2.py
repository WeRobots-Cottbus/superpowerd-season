
import time

def run():
    print(f"run slave 2")
    for i in range(10):
        print(f" slave 2: do step {i}")
        time.sleep(0.15)
    print(f"slave 2 finished")

if __name__ == "__main__":
    run()
