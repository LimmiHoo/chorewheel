# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ChoreWheel
import unittest
from chorewheel.models import Chore, ChoreAssignment, ChoreSchedule, ChoreStreak, ChoreReminder
from chorewheel.services import ChoreSearchService, ChoreFilterService


class TestChoreSearchService(unittest.TestCase):
    def setUp(self):
        self.chore_service = ChoreSearchService()

    def test_search_by_name_case_insensitive(self):
        chore = Chore(name="Dishes", duration_minutes=30)
        self.chore_service.add_chore(chore)
        results = self.chore_service.search("dishes")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Dishes")

    def test_search_by_category(self):
        chore = Chore(name="Clean Kitchen", category="Cleaning", duration_minutes=45)
        self.chore_service.add_chore(chore)
        results = self.chore_service.search(category="Cleaning")
        self.assertEqual(len(results), 1)

    def test_search_by_duration_range(self):
        chore = Chore(name="Quick Task", duration_minutes=15)
        self.chore_service.add_chore(chore)
        results = self.chore_service.search(min_duration=10, max_duration=20)
        self.assertEqual(len(results), 1)


class TestChoreFilterService(unittest.TestCase):
    def setUp(self):
        self.filter_service = ChoreFilterService()

    def test_filter_by_frequency(self):
        chore = Chore(name="Water Plants", frequency="Weekly")
        self.filter_service.add_chore(chore)
        filtered = self.filter_service.filter(frequency="Weekly")
        self.assertEqual(len(filtered), 1)

    def test_filter_by_priority(self):
        chore = Chore(name="Important Task", priority="High")
        self.filter_service.add_chore(chore)
        filtered = self.filter_service.filter(priority="High")
        self.assertEqual(len(filtered), 1)

    def test_combined_filters(self):
        chore1 = Chore(name="Task A", frequency="Daily", priority="High")
        chore2 = Chore(name="Task B", frequency="Weekly", priority="Low")
        self.filter_service.add_chore(chore1)
        self.filter_service.add_chore(chore2)
        filtered = self.filter_service.filter(frequency="Weekly", priority="High")
        self.assertEqual(len(filtered), 0)


if __name__ == "__main__":
    unittest.main()
