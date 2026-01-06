from pynput import keyboard

from interactions.keyboard_listener import KeyboardListener
from interactions.mouse_controller import MouseController

if __name__ == '__main__':
    kbl = KeyboardListener(keyboard.Key.ctrl_l)

    while (True):
        kbl.process_keys()
