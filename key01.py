from pynput.keyboard import *
import time


keyboard = Controller()



time.sleep(5)

for i in range(0,1000):

    #keyboard.press(Key.down)
    keyboard.press('a')
    #keyboard.press(Key.left)

    time.sleep(0.02)


keyboard.release('a')
#keyboard.release(Key.left)

for i in range(0,500):
    #keyboard.press(Key.down)
    keyboard.press('a')
    #keyboard.press(Key.right)

    time.sleep(0.02)


keyboard.release('a')
#keyboard.release(Key.right)
for i in range(0,150):
    keyboard.press(Key.down)
    #keyboard.press('a')

    time.sleep(0.02)

keyboard.release(Key.down)
