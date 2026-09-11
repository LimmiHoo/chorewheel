# === Stage 24: Add grouped summaries by category or status ===
# Project: ChoreWheel
def grouped_summaries(assignments):
    by_cat = {}
    by_status = {}
    for a in assignments:
        by_cat.setdefault(a["category"], []).append(a)
        by_status.setdefault(a["status"], []).append(a)
    return {"by_category": by_cat, "by_status": by_status}
