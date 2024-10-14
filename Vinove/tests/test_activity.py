import unittest
from activity_tracker import ActivityTracker

class TestActivityTracker(unittest.TestCase):
    def test_detect_genuine_activity(self):
        tracker = ActivityTracker()
        self.assertFalse(tracker.detect_genuine_activity())  # Assuming no activity

if __name__ == "__main__":
    unittest.main()