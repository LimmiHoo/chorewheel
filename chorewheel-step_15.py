# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ChoreWheel
def handle_command(text: str, chores: dict) -> str:
    """Parse a user text command and return a response."""
    text = text.strip().lower()
    if text.startswith("add"):
        parts = text.split(None, 2)
        if len(parts) >= 3:
            name, freq, person = parts[1].title(), parts[2].title(), "you"
            chores[name] = {"frequency": freq, "person": person, "done": []}
            return f"Added chore: {name} ({freq} by {person})"
        return "Usage: add <name> <frequency> <person>"
    if text.startswith("schedule"):
        for name, info in chores.items():
            if info["frequency"] == "weekly":
                return f"Scheduled: {name} every Sunday"
            elif info["frequency"] == "daily":
                return f"Scheduled: {name} every day"
            elif info["frequency"] == "monthly":
                return f"Scheduled: {name} every 1st of the month"
        return "No chores to schedule yet"
    if text.startswith("streak"):
        for name, info in chores.items():
            if info["person"] == "you":
                done = info["done"]
                return f"Your streak: {len(done)} completed {name}"
        return "No personal chores to track"
    if text.startswith("list"):
        return "\n".join(f"- {name}: {info['frequency']} by {info['person']}" for name, info in chores.items())
    if text.startswith("done"):
        parts = text.split(None, 2)
        if len(parts) >= 2:
            name = parts[1].title()
            if name in chores:
                chores[name]["done"].append("now")
                return f"Marked {name} as done"
            return "Chore not found"
        return "Usage: done <chore_name>"
    return "Unknown command. Try: add, schedule, streak, list, done"
