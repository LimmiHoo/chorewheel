# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ChoreWheel
import unittest
from chorewheel.models import Chore, ChoreAssignment
from chorewheel.helpers import create_default_schedule, validate_chore_assignment


class TestHelpers(unittest.TestCase):
    def test_create_default_schedule(self):
        schedule = create_default_schedule()
        self.assertIsInstance(schedule, dict)
        self.assertIn("rotation_period_days", schedule)
        self.assertIn("default_reminder_time", schedule)
        self.assertEqual(schedule["rotation_period_days"], 7)
        self.assertEqual(schedule["default_reminder_time"], "20:00")

    def test_validate_chore_assignment_valid(self):
        assignment = ChoreAssignment(
            name="Dishes",
            owner="Alice",
            frequency="weekly",
            next_due="2024-12-30",
            streak=3,
            priority=2,
            notes="Use dishwasher when possible",
        )
        result = validate_chore_assignment(assignment)
        self.assertTrue(result["valid"])
        self.assertEqual(result["message"], "Valid assignment.")

    def test_validate_chore_assignment_invalid_frequency(self):
        assignment = ChoreAssignment(
            name="Bad",
            owner="Bob",
            frequency="invalid",
            next_due="2024-12-30",
            streak=0,
            priority=1,
            notes="",
        )
        result = validate_chore_assignment(assignment)
        self.assertFalse(result["valid"])
        self.assertIn("Invalid frequency", result["message"])

    def test_validate_chore_assignment_missing_owner(self):
        assignment = ChoreAssignment(
            name="NoOwner",
            owner="",
            frequency="weekly",
            next_due="2024-12-30",
            streak=0,
            priority=1,
            notes="",
        )
        result = validate_chore_assignment(assignment)
        self.assertFalse(result["valid"])
        self.assertIn("Owner name is required", result["message"])


if __name__ == "__main__":
    unittest.main()
