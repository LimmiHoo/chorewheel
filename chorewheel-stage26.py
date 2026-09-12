# === Stage 26: Add weekly summary calculations ===
# Project: ChoreWheel
from datetime import date, timedelta

def weekly_summary(chore_log: dict) -> dict:
    """Return a compact weekly summary: total chores, per-day counts, and longest streak."""
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    days = {week_start + timedelta(days=i).strftime("%A"): 0 for i in range(7)}
    for entry in chore_log:
        d = date.fromisoformat(entry["date"])
        if week_start <= d <= today:
            days[d.strftime("%A")] += 1
    longest = max(days.values(), default=0)
    return {"week_chores": sum(days.values()), "day_counts": days, "longest_streak": longest}
