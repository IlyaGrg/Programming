import threading
import time
import random
import string

data = []
lock = threading.Lock()


def generate_string(length):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def printer():
    while True:
        with lock:
            snapshot = list(data)
        print(snapshot)
        time.sleep(1)


def sorter():
    while True:
        time.sleep(5)
        with lock:
            data.sort()
            snapshot = list(data)
        with open("out.txt", "w") as f:
            f.write(" ".join(snapshot))


t1 = threading.Thread(target=printer, daemon=True)
t2 = threading.Thread(target=sorter, daemon=True)
t1.start()
t2.start()


try:
    while True:
        s = generate_string(10)
        with lock:
            data.append(s)
        time.sleep(1)
except KeyboardInterrupt:
    print("Остановлено")
