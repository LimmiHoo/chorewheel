# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ChoreWheel
def get_upcoming_items(items, now=None):
    """Return items due within the next 7 days, sorted by due date."""
    if now is None:
        from datetime import datetime, timedelta
        now = datetime.now()
    cutoff = now + timedelta(days=7)
    upcoming = sorted(
        [i for i in items if i.get("due_date") and i["due_date"] <= cutoff],
        key=lambda i: i["due_date"],
    )
    return upcoming


def get_overdue_items(items, now=None):
    """Return items past their due date."""
    if now is None:
        from datetime import datetime
        now = datetime.now()
    overdue = sorted(
        [i for i in items if i.get("due_date") and i["due_date"] < now],
        key=lambda i: i["due_date"],
    )
    return overdue


def get_due_today_items(items, now=None):
    """Return items due today (including now)."""
    if now is None:
        from datetime import datetime
        now = datetime.now()
    today = now.date()
    due_today = [
        i for i in items
        if i.get("due_date") and i["due_date"].date() == today
    ]
    return due_today


def get_due_soon_items(items, now=None, days_ahead=3):
    """Return items due within a given number of days."""
    if now is None:
        from datetime import datetime, timedelta
        now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    due_soon = sorted(
        [i for i in items if i.get("due_date") and i["due_date"] <= cutoff],
        key=lambda i: i["due_date"],
    )
    return due_soon
