# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ChoreWheel
from datetime import date, timedelta

def parse_date(raw):
    """Parse a date string in YYYY-MM-DD or MM/DD/YYYY format.
    Raises ValueError with a clear message on failure.
    """
    if not raw or not raw.strip():
        raise ValueError("Date string is empty or missing.")

    raw = raw.strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y"):
        try:
            return date(*map(int, raw.split(fmt.replace("-", "/"))))
        except (ValueError, IndexError):
            continue
    raise ValueError(f"Unrecognized date format: '{raw}'. Use YYYY-MM-DD or MM/DD/YYYY.")
