# === Stage 67: Add a function that returns key project metrics ===
# Project: ChoreWheel
import datetime

def project_metrics(assignments, schedules, streaks, reminders):
    """Return key metrics for the ChoreWheel project."""
    total_assignments = len(assignments)
    active_schedules = sum(1 for s in schedules if s["active"])
    total_streaks = sum(s["streak"] for s in streaks.values())
    completed_reminders = sum(1 for r in reminders.values() if r["completed"])
    today = datetime.date.today()
    overdue = sum(1 for a in assignments if a["due"] < today and not a["completed"])
    return {
        "total_assignments": total_assignments,
        "active_schedules": active_schedules,
        "total_streaks": total_streaks,
        "completed_reminders": completed_reminders,
        "overdue_assignments": overdue,
    }
