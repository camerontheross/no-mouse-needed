from pynput import keyboard


class KeyboardListener():

    def __init__(self, leader_key, directions):

        self.leader_key = leader_key
        self.directions = directions
        self.can_listen = False
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()

    def __del__(self):

        self.listener.stop()

    def on_press(self, key):

        if key == self.leader_key:
            self.can_listen = True

        if not self.can_listen:
            return
        print(key, type(key))

    def on_release(self, key):

        if key == self.leader_key:
            self.can_listen = False
        print(key, "released")
