# === Stage 14: Add file load support with fallback demo data ===
# Project: ChoreWheel
# ── File Load with Fallback Demo Data ──
import os, json

def load_file(path: str, default=None):
    """Read a JSON file; return *default* if missing or malformed."""
    if not os.path.isfile(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return default
    return data

def load_schedule(path: str, default=None):
    """Load schedule JSON; fall back to a built-in demo."""
    demo = {
        "assignments": [
            {"name": "Dishes", "owner": "Alice", "frequency": "daily"},
            {"name": "Vacuum", "owner": "Bob", "frequency": "weekly"},
            {"name": "Laundry", "owner": "Charlie", "frequency": "twice_weekly"},
            {"name": "Trash", "owner": "Dana", "frequency": "weekly"},
        ],
        "schedule": [
            {"day": "Monday", "tasks": ["Dishes", "Vacuum"]},
            {"day": "Wednesday", "tasks": ["Laundry"]},
            {"day": "Saturday", "tasks": ["Trash"]},
        ],
        "streaks": {"Alice": 12, "Bob": 8, "Charlie": 5, "Dana": 3},
    }
    return load_file(path, default=demo)
