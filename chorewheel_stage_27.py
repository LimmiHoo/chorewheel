# === Stage 27: Add monthly summary calculations ===
# Project: ChoreWheel
def monthly_summary(schedule):
    """Compute a monthly summary of chore completion for a given schedule."""
    month = datetime.date.today().month
    summary = {}
    for assign, freq in schedule.items():
        if assign not in summary:
            summary[assign] = {"completed": 0, "expected": 0}
        for day in range(1, 32):
            if (day, month) in schedule[assign]:
                summary[assign]["expected"] += 1
                if (day, month) in schedule[assign]:
                    summary[assign]["completed"] += 1
    return summary
