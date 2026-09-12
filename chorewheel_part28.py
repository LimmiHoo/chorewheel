# === Stage 28: Add overdue item detection based on due dates ===
# Project: ChoreWheel
def detect_overdue(assignments):
    overdue = []
    today = datetime.now().date()
    for item in assignments:
        due = item.get("due_date")
        if due and due < today:
            overdue.append({"item": item, "days_overdue": (today - due).days})
    return overdue
