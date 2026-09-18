# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ChoreWheel
import pytest
from chorewheel.models import Assignment, Schedule, Streak, Reminder
from chorewheel.schedules import Scheduler
from chorewheel.reminders import ReminderManager
from datetime import datetime, timedelta

def test_update_assignment_removes_old_schedule():
    sched = Scheduler()
    sched.add_assignment(Assignment("wash_dishes", "Alice", 3))
    sched.add_assignment(Assignment("sweep_floor", "Bob", 5))
    assert sched.schedule["wash_dishes"] == 3
    sched.update_assignment("wash_dishes", 7)
    assert sched.schedule["wash_dishes"] == 7
    assert sched.schedule["sweep_floor"] == 5

def test_delete_assignment_removes_all_related():
    sched = Scheduler()
    sched.add_assignment(Assignment("vacuum", "Alice", 4))
    sched.add_assignment(Assignment("clean_toilet", "Bob", 3))
    sched.delete_assignment("vacuum")
    assert "vacuum" not in sched.schedule
    assert sched.schedule["clean_toilet"] == 3

def test_update_removes_old_reminder():
    rm = ReminderManager()
    rm.schedule_reminder("vacuum", "Alice", 4, 2)
    rm.schedule_reminder("clean_toilet", "Bob", 3, 1)
    rm.update_reminder("vacuum", "Alice", 2, 3)
    assert rm.reminders["vacuum"] == {"who": "Alice", "days": 3}
    assert "clean_toilet" in rm.reminders
