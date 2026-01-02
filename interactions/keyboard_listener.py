from pynput import keyboard
from pynput.keyboard import Key, KeyCode


class KeyboardListener():

    def __init__(self, leader_key: Key, directions):

        self.leader_key = leader_key
        self.directions = directions

        self.pressed_keys: list[Key] = []

        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()

    def __del__(self):

        self.listener.stop()

    def on_press(self, key):


        print(key, type(key))

    def on_release(self, key):
        pass


    def can_listen(self) -> bool:

        if self.leader_key in self.pressed_keys:
            return True

        return False
