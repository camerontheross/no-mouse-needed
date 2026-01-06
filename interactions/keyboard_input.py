from pynput import keyboard


class KeyboardInput():

    def __init__(self):

        self.leader_key = None

        self.key_buffer: list[keyboard.Key] = []

        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()

    def __del__(self):

        self.listener.stop()

    def on_press(self, key):

        if key not in self.key_buffer:
            self.key_buffer.append(key)

    def on_release(self, key):

        if key in self.key_buffer:
            self.key_buffer.remove(key)

    def can_listen(self) -> bool:

        if self.leader_key in self.key_buffer:
            return True

        return False

    def get_buffer(self) -> list[keyboard.Key]:

        if not self.can_listen():
            return []

        return self.key_buffer
