# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ChoreWheel
def update_assignment(assignment_id, **kwargs):
    """Update an assignment's fields. Returns the updated record or None if not found."""
    record = _find_assignment(assignment_id)
    if record is None:
        raise ValueError(f"Assignment {assignment_id} not found")
    for key, value in kwargs.items():
        setattr(record, key, value)
    record.save()
    return record

def update_schedule(schedule_id, **kwargs):
    """Update a schedule's fields. Returns the updated record or None if not found."""
    record = _find_schedule(schedule_id)
    if record is None:
        raise ValueError(f"Schedule {schedule_id} not found")
    for key, value in kwargs.items():
        setattr(record, key, value)
    record.save()
    return record

def update_streak(streak_id, **kwargs):
    """Update a streak's fields. Returns the updated record or None if not found."""
    record = _find_streak(streak_id)
    if record is None:
        raise ValueError(f"Streak {streak_id} not found")
    for key, value in kwargs.items():
        setattr(record, key, value)
    record.save()
    return record

def update_reminder(reminder_id, **kwargs):
    """Update a reminder's fields. Returns the updated record or None if not found."""
    record = _find_reminder(reminder_id)
    if record is None:
        raise ValueError(f"Reminder {reminder_id} not found")
    for key, value in kwargs.items():
        setattr(record, key, value)
    record.save()
    return record
