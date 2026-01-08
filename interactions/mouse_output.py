from pynput.mouse import Button, Controller

from utils.vector2 import Vector2


class MouseOutput():

    def __init__(self, sensitivity: int):
        self.mouse = Controller()
        self.sensitivity = sensitivity
        self.pressed_buttons: list[Button] = []

    def __del__(self):

        for button in self.pressed_buttons:
            self.mouse.release(button)

    def move_mouse(self, direction: Vector2):

        x_delta = direction.x * self.sensitivity
        y_delta = direction.y * self.sensitivity

        self.mouse.move(x_delta, y_delta)

    def click(self, button: Button):
        self.mouse.press(button=button)

        if button not in self.pressed_buttons:
            self.pressed_buttons.append(button)

    def release(self, button: Button):
        self.mouse.release(button=button)

        if button in self.pressed_buttons:
            self.pressed_buttons.remove(button)
