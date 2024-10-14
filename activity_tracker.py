import threading
import time
from screenshot_handler import ScreenshotHandler

class ActivityTracker:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.screenshot_handler = ScreenshotHandler()
        self.running = True

    def track_activity(self):
        while self.running:
            # Simulate user activity check
            time.sleep(1)  # Replace with actual activity detection logic
            if self.config_manager.screenshot_enabled:
                self.screenshot_handler.capture_screenshot()

    def start_tracking(self):
        threading.Thread(target=self.track_activity).start()

    def stop(self):
        self.running = False
