# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ChoreWheel
# chorewheel.py — append this block at the end of the existing file

ANSI = {
    "RESET": "\033[0m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "CYAN": "\033[36m",
    "BOLD": "\033[1m",
    "DIM": "\033[2m",
}

def colorize(text: str, color: str) -> str:
    return f"{ANSI[color]}{text}{ANSI['RESET']}"

def header(text: str) -> str:
    return colorize(f"\n{'=' * 60}", "CYAN") + "\n" + colorize(text, "BOLD") + "\n"

def success(text: str) -> str:
    return colorize(text, "GREEN")

def warning(text: str) -> str:
    return colorize(text, "YELLOW")

def error_out(text: str) -> str:
    return colorize(text, "RED")

def info(text: str) -> str:
    return colorize(text, "BLUE")

def dim(text: str) -> str:
    return colorize(text, "DIM")

def print_schedule(chore: dict) -> str:
    return (
        header(f"  {chore['name']}")
        + dim(f"  Assigned to: {chore['who']}")
        + dim(f"  Schedule:    {chore['day']}")
    )

def print_streak(streak: int) -> str:
    if streak > 5:
        return colorize(f"  Streak: {streak} days", "GREEN")
    elif streak > 2:
        return colorize(f"  Streak: {streak} days", "YELLOW")
    return colorize(f"  Streak: {streak} days", "DIM")

def print_reminder(chore: dict) -> str:
    return (
        header(f"  Reminder: {chore['name']}")
        + success(f"  Due: {chore['due']}")
    )
