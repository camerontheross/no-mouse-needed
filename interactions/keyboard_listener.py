from pynput import keyboard


class KeyboardListener():

    def __init__(self, leader_key: keyboard.Key):

        self.leader_key = leader_key

        self.pressed_keys: list[keyboard.Key] = []

        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()

    def __del__(self):

        self.listener.stop()

    def on_press(self, key):

        if key not in self.pressed_keys:
            self.pressed_keys.append(key)

    def on_release(self, key):

        if key in self.pressed_keys:
            self.pressed_keys.remove(key)

    def can_listen(self) -> bool:

        if self.leader_key in self.pressed_keys:
            return True

        self.pressed_keys.clear()
        return False

    def process_keys(self):

        if not self.can_listen():
            return
        print(self.pressed_keys)
