
import time

def run():
    print(f"run slave 3")
    for i in range(15):
        print(f" slave 3: do step {i}")
        time.sleep(0.5)
    print(f"slave 3 finished")

if __name__ == "__main__":
    run()
