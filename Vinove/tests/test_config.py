import unittest
from config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):
    def test_fetch_config(self):
        config = ConfigManager()
        self.assertIn("interval", config.fetch_config())

if __name__ == "__main__":
    unittest.main()