import threading
import time
from tkinter import Tk
from activity_tracker import ActivityTracker
from config_manager import ConfigManager

def main():
    # Load configurations
    config_manager = ConfigManager()
    config_manager.load_config()

    # Initialize activity tracker
    tracker = ActivityTracker(config_manager)
    tracker.start_tracking()

    # Start GUI (if needed, can be expanded)
    root = Tk()
    root.title("Employee Activity Tracker")
    root.geometry("300x200")
    root.mainloop()

if __name__ == "__main__":
    main()
