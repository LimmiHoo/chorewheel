# === Stage 66: Add export of a short status dashboard ===
# Project: ChoreWheel
def status_dashboard(assignments, schedules, streaks, reminders):
    """Compact status dashboard for ChoreWheel."""
    lines = []
    lines.append("=== ChoreWheel Dashboard ===")
    lines.append(f"Assignments: {len(assignments)}")
    lines.append(f"Schedules: {len(schedules)}")
    lines.append(f"Streaks: {len(streaks)}")
    lines.append(f"Reminders: {len(reminders)}")
    if assignments:
        lines.append(f"\nSample Assignment: {assignments[0].get('name', 'N/A')}")
    if schedules:
        lines.append(f"\nSample Schedule: {schedules[0].get('day', 'N/A')}")
    if streaks:
        lines.append(f"\nSample Streak: {streaks[0].get('chore', 'N/A')} - {streaks[0].get('count', 0)} days")
    if reminders:
        lines.append(f"\nSample Reminder: {reminders[0].get('chore', 'N/A')} on {reminders[0].get('date', 'N/A')}")
    return "\n".join(lines)
