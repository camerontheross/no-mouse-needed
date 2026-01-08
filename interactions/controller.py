from interactions.keyboard_input import KeyboardInput
from interactions.mouse_output import MouseOutput
from utils.settings_loader import SettingsLoader
from utils.vector2 import Vector2


class Controller():

    def __init__(self):

        self.settings = SettingsLoader()

        self.input = KeyboardInput(self.settings.get_leader_key())
        self.output = MouseOutput(self.settings.get_sensitivity())

        self.controls = self.settings.get_controls()

    def process_key_buffer(self):

        input_buffer = self.input.get_buffer()

        if not input_buffer:
            return

        movement_direction = self.get_move_direction(input_buffer)

        self.output.move_mouse(movement_direction)


    def get_move_direction(self, input_buffer) -> Vector2:

        direction = Vector2()

        if self.controls["CURSOR_UP"] in input_buffer:
            direction.y -= 1

        if self.controls["CURSOR_DOWN"] in input_buffer:
            direction.y += 1

        if self.controls["CURSOR_LEFT"] in input_buffer:
            direction.x -= 1

        if self.controls["CURSOR_RIGHT"] in input_buffer:
            direction.x += 1

        return direction
