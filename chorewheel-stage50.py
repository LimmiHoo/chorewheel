# === Stage 50: Add unit tests for import and export behavior ===
# Project: ChoreWheel
import json, os, tempfile, unittest
from chorewheel import ChoreWheel

class TestWheelIO(unittest.TestCase):
    def setUp(self):
        self.w = ChoreWheel()
        self.w.add_assignment("Dishes", "Alice")
        self.w.add_assignment("Vacuum", "Bob")
        self.w.set_schedule("weekly")
        self.w.add_reminder("Dishes", "18:00")

    def test_json_roundtrip(self):
        path = os.path.join(tempfile.gettempdir(), "chorewheel.json")
        self.w.save(path)
        loaded = ChoreWheel.load(path)
        self.assertEqual(loaded.assignments, self.w.assignments)
        self.assertEqual(loaded.schedule, "weekly")
        self.assertEqual(loaded.reminders, {"Dishes": "18:00"})
        os.remove(path)

    def test_export_csv(self):
        csv_path = os.path.join(tempfile.gettempdir(), "chorewheel.csv")
        self.w.export_csv(csv_path)
        with open(csv_path) as f:
            lines = f.read().strip().splitlines()
        self.assertTrue(len(lines) >= 2)
        self.assertIn("Dishes", lines[0])
        os.remove(csv_path)
