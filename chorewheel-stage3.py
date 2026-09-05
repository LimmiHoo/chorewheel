# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ChoreWheel
VALID_ID_CHARS = set('abcdefghijklmnopqrstuvwxyz0123456789-')
MAX_NAME_LEN = 80
MAX_DESC_LEN = 300
MAX_STREAK = 100

def is_valid_id(value):
    if not isinstance(value, str) or not value:
        return False
    return all(c in VALID_ID_CHARS for c in value)

def validate_name(value):
    if not isinstance(value, str) or not value or len(value) > MAX_NAME_LEN:
        return False
    stripped = value.strip()
    return len(stripped) > 0

def validate_description(value):
    if not isinstance(value, str):
        return False
    if len(value) > MAX_DESC_LEN:
        return False
    return True

def validate_streak(value):
    if not isinstance(value, int) or value < 0 or value > MAX_STREAK:
        return False
    return True

def validate_date(value):
    if not isinstance(value, str):
        return False
    try:
        from datetime import datetime
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False
