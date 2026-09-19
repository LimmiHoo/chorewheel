# === Stage 55: Add a setting to disable colorized output ===
# Project: ChoreWheel
import os

def disable_color():
    """Disable ANSI color codes in terminal output."""
    if not os.environ.get("NO_COLOR"):
        os.environ["NO_COLOR"] = "1"
