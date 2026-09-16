# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ChoreWheel
def parse_line(chore_line):
    """Parse a single chore entry from a simple line-based format.

    Expected format:
        chore_name|assignee|frequency|days_of_week

    Args:
        chore_line (str): A single line of chore data.

    Returns:
        dict: A dictionary containing chore_name, assignee, frequency, and days_of_week.

    Raises:
        ValueError: If the line is empty or does not have exactly four fields.
    """
    if not chore_line or not chore_line.strip():
        raise ValueError("Empty line encountered")

    parts = chore_line.strip().split('|')
    if len(parts) != 4:
        raise ValueError(
            f"Expected 4 fields separated by '|', got {len(parts)}: {chore_line}"
        )

    chore_name = parts[0].strip()
    assignee = parts[1].strip()
    frequency = parts[2].strip()
    days_of_week = parts[3].strip()

    return {
        'chore_name': chore_name,
        'assignee': assignee,
        'frequency': frequency,
        'days_of_week': days_of_week,
    }
