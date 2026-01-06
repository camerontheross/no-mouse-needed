
class SettingsLoader():

    def __init__(self):
        pass

    def load_settings_json(self):

        try:
            with open("settings.json", "r") as settings:
                print(settings)
        except FileNotFoundError:
            print("No settings found. Initializing default settings.")
        except PermissionError:
            print("Error: Could not access settings file due to permissions.")
            print("Change permissions and try again.")
