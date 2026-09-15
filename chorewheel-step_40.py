# === Stage 40: Add plain text report export ===
# Project: ChoreWheel
def export_report(chore_wheel):
    """Export a plain-text summary of the chore wheel state."""
    lines = []
    lines.append("ChoreWheel Report")
    lines.append("=" * 40)
    lines.append(f"Active assignments: {len(chore_wheel.assignments)}")
    lines.append(f"Completed today: {len(chore_wheel.completed_today)}")
    lines.append(f"Streaks: {len(chore_wheel.streaks)}")
    if chore_wheel.reminders:
        lines.append(f"Reminders: {len(chore_wheel.reminders)}")
    lines.append("")
    for name, count in sorted(chore_wheel.assignments.items()):
        lines.append(f"{name}: {count}")
    lines.append("=" * 40)
    return "\n".join(lines)
