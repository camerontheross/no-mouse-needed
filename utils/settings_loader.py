
class SettingsLoader():

    def __init__(self):
        pass

    def load_settings_json(self):

        try:
            with open("~/settings.json", "r") as settings:
                print(settings)
        except FileNotFoundError:
            print("No settings found. Initializing default settings.")
            self.init_default_settings()
        except PermissionError:
            print("Error: Could not access settings file due to permissions.")
            print("Change permissions for settings.json and try again.")

    def init_default_settings(self):
        pass
