# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ChoreWheel
def sort_chores(chore_list, key_func=None):
    if key_func is None:
        key_func = lambda c: (c.get("priority", 0), c.get("due_date"), c.get("title", ""))
    return sorted(chore_list, key=key_func)
