# === Stage 38: Add data integrity checks for broken references ===
# Project: ChoreWheel
def check_references(data):
    """Validate that all foreign keys in chore assignments and schedules are intact."""
    assignments = data.get("assignments", [])
    schedules = data.get("schedules", [])
    valid_members = {m["name"] for m in data.get("members", [])}
    valid_chores = {c["name"] for c in data.get("chore_names", [])}
    valid_reminders = {r["name"] for r in data.get("reminder_names", [])}
    errors = []
    for a in assignments:
        if a.get("member") not in valid_members:
            errors.append(f"Assignment references unknown member: {a.get('member')}")
        if a.get("chore") not in valid_chores:
            errors.append(f"Assignment references unknown chore: {a.get('chore')}")
        if a.get("reminder") not in valid_reminders:
            errors.append(f"Assignment references unknown reminder: {a.get('reminder')}")
    for s in schedules:
        if s.get("member") not in valid_members:
            errors.append(f"Schedule references unknown member: {s.get('member')}")
        if s.get("chore") not in valid_chores:
            errors.append(f"Schedule references unknown chore: {s.get('chore')}")
    return errors
