# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ChoreWheel
def _format_assignment_display(assignment):
    """Return a human-readable summary for an assignment."""
    return (
        f"[{assignment['name']}] "
        f"{assignment['owner']} "
        f"({assignment['days']}) "
        f"→ {assignment['next_due']}"
    )


def _format_weekly_schedule(schedule):
    """Return a human-readable weekly schedule string."""
    lines = ["Weekday\t\tChore\t\tAssigned To"]
    for row in schedule:
        lines.append(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")
    return "\n".join(lines)


def _format_streak_summary(streak):
    """Return a human-readable streak summary for a user."""
    return (
        f"{streak['user']} "
        f"completed {streak['count']} chores "
        f"in a row ({streak['percent']}% weekly)"
    )


def _format_reminder_message(reminder):
    """Return a human-readable reminder message."""
    return (
        f"⏰ Reminder: {reminder['text']} "
        f"due {reminder['due']} "
        f"for {reminder['assigned_to']}"
    )
