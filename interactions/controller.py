from keyboard_input import KeyboardInput
from mouse_output import MouseOutput

from utils.vector2 import Vector2


class Controller():

    def __init__(self):

        self.input = KeyboardInput()
        self.output = MouseOutput()

    def process_key_buffer(self):

        input_buffer = self.input.get_buffer()

        movement_direction = self.get_move_direction()

        self.output.move_mouse(movement_direction)



    def get_move_direction(self) -> Vector2:
        return Vector2()
