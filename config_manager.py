import json

class ConfigManager:
    def __init__(self):
        self.screenshot_enabled = True
        self.screenshot_interval = 300  # Default to 5 minutes

    def load_config(self):
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
                self.screenshot_enabled = config.get('screenshot_enabled', True)
                self.screenshot_interval = config.get('screenshot_interval', 300)
        except FileNotFoundError:
            self.save_default_config()

    def save_default_config(self):
        default_config = {
            'screenshot_enabled': self.screenshot_enabled,
            'screenshot_interval': self.screenshot_interval
        }
        with open('config.json', 'w') as file:
            json.dump(default_config, file)