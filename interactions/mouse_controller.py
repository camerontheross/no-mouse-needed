from pynput.mouse import Button, Controller


class MouseController():

    def __init__(self, sensitivity):
        self.mouse = Controller()
        self.sensitivity = sensitivity

    def move_mouse(self, x_delta, y_delta):
        self.mouse.move(x_delta * self.sensitivity, y_delta * self.sensitivity)

    def right_click(self):
        pass

    def left_click(self):
        pass

    def middle_click(self):
        pass
