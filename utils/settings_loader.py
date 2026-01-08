import json

from pynput import keyboard


class SettingsLoader():

    def __init__(self):

        self.settings = self.load_settings_json()

    def load_settings_json(self) -> dict:

        try:
            with open("settings.json", "r") as settings:

                return json.load(settings)

        except FileNotFoundError:

            print("No settings found. Initializing default settings.")
            return self.init_default_settings()

        except PermissionError:

            print("Error: Could not access settings file due to permissions.")
            print("Change permissions for settings.json and try again.")
            exit()

    def init_default_settings(self) -> dict:

        default_settings = {
            "leader": "<ctrl_r>",
            "sensitivity": 0.5,
            "controls": {

                "CURSOR_UP": "w",
                "CURSOR_DOWN": "s",
                "CURSOR_LEFT": "a",
                "CURSOR_RIGHT": "d",

                "LEFT_CLICK": "q",
                "RIGHT_CLICK": "e",
                "MIDDLE_CLICK": "r"
            }
        }

        with open('settings.json', 'w') as settings_file:

            json.dump(default_settings, settings_file, indent=4)

        return default_settings

    def get_controls(self) -> dict:

        try:

            controls = self.settings["controls"]

            for key, value in controls.items():
                controls[key] = keyboard.KeyCode().from_char(value)

            return controls

        except KeyError:

            self.init_default_settings()

            print("Controls could not be found in settings.")
            print("Returning default controls.")

            return self.get_controls()

    def get_sensitivity(self) -> int:

        try:

            sensitvity = self.settings["sensitivity"]
            return sensitvity

        except KeyError:

            self.init_default_settings()

            print("Sensitivity could not be found in settings.")
            print("Returning default sensitivity.")

            return self.get_sensitivity()

    def get_leader_key(self) -> keyboard.Key:

        try:

            leader = self.settings["leader"]

            leader_key = keyboard.Key(keyboard.HotKey.parse(leader)[0])

            return leader_key

        except KeyError:

            self.init_default_settings()

            print("Leader could not be found in settings.")
            print("Returning default leader.")

            return self.get_leader_key()
