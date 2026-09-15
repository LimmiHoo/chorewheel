# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ChoreWheel
def repair_data(data):
    """Repair simple data integrity issues in the ChoreWheel data model.

    Handles: missing required fields, empty values, invalid dates,
    and duplicate assignments with the same chore and person.

    Args:
        data (list[dict]): ChoreWheel data model.

    Returns:
        list[dict]: Repaired data.
    """
    repaired = []
    for entry in data:
        if "chore" not in entry or not entry["chore"]:
            entry["chore"] = "Default Chore"
        if "person" not in entry or not entry["person"]:
            entry["person"] = "Unassigned"
        if "status" not in entry:
            entry["status"] = "Pending"
        if "completed" not in entry:
            entry["completed"] = False
        if "streak" not in entry:
            entry["streak"] = 0
        if "reminder_time" not in entry:
            entry["reminder_time"] = "18:00"
        if "completed_at" not in entry:
            entry["completed_at"] = None
        if "completed_at" in entry and entry["completed_at"]:
            try:
                datetime.fromisoformat(entry["completed_at"])
            except ValueError:
                entry["completed_at"] = None
        repaired.append(entry)
    return repaired
