# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ChoreWheel
DEFAULT_SETTINGS = {
    "reminder_hour": 8,
    "reminder_minute": 0,
    "weekend_chore_enabled": True,
    "streak_threshold": 5,
    "streak_decay": 0.2,
    "language": "en",
    "theme": "light",
}

def get_settings():
    return _load_settings()

def set_setting(key, value):
    if key not in DEFAULT_SETTINGS:
        raise ValueError(f"Unknown setting: {key}")
    _load_settings()[key] = value

def toggle_weekend_chore():
    settings = _load_settings()
    settings["weekend_chore_enabled"] = not settings["weekend_chore_enabled"]

def reset_settings():
    _save_settings(DEFAULT_SETTINGS.copy())
