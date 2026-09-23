# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ChoreWheel
def clear_state():
    """Reset the ChoreWheel to a clean slate.
    
    Requires a confirmation flag to prevent accidental data loss.
    """
    if not _CONFIRMED:
        raise PermissionError("Clear state requires confirmation. Set _CONFIRMED = True first.")
    
    _CONFIRMED = False
    _assignments = []
    _schedules = {}
    _streaks = {}
    _reminders = []
    _last_reset = datetime.now()
    _history_log = []
    
    return {
        "assignments": _assignments,
        "schedules": _schedules,
        "streaks": _streaks,
        "reminders": _reminders,
        "last_reset": _last_reset,
        "history": _history_log,
    }
