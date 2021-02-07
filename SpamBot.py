import random
from pynput.keyboard import Controller, Key
import time
keyboard = Controller()

file = "MessageFile.txt"
fr = open(file, "r")
print("Reading file")
messages = fr.readlines()
print("spamming in 5")
time.sleep(5)
i = 0
while True:
    keyboard.type(random.choice(messages))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print(i)
    i = i + 1
    time.sleep(0.7)

