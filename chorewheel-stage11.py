# === Stage 11: Add JSON export for the current application state ===
# Project: ChoreWheel
def export_to_json(path: str = "chorewheel_state.json"):
    """Export the entire ChoreWheel state to a JSON file."""
    import json
    from datetime import datetime

    state = {
        "assignments": assignments,
        "schedule": schedule,
        "streaks": streaks,
        "reminders": reminders,
        "completed": completed,
        "exported_at": datetime.now().isoformat(),
    }
    with open(path, "w") as f:
        json.dump(state, f, indent=2)
    print(f"State exported to {path}")
