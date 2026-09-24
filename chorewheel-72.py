# === Stage 72: Add Markdown report export ===
# Project: ChoreWheel
def export_report(self, filename="chore_report.md"):
    """Generate a Markdown report of all chores and their status."""
    lines = ["# ChoreWheel Report", ""]
    lines.append("## Completed\n")
    for chore in self.chore_db["completed"]:
        lines.append(f"- **{chore['name']}** by {chore['assigned_to']} at {chore['completed_at']}")
    lines.append("")
    lines.append("## In Progress\n")
    for chore in self.chore_db["in_progress"]:
        lines.append(f"- **{chore['name']}** assigned to {chore['assigned_to']}")
    lines.append("")
    lines.append("## Upcoming\n")
    for chore in self.chore_db["upcoming"]:
        lines.append(f"- **{chore['name']}** by {chore['assigned_to']} on {chore['scheduled_date']}")
    lines.append("")
    lines.append("## Streaks\n")
    for user, streak in self.chore_db["streaks"].items():
        lines.append(f"- **{user}**: {streak} days")
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    print(f"Report saved to {filename}")
