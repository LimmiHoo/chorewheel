# === Stage 42: Add CSV export without external dependencies ===
# Project: ChoreWheel
import csv
from datetime import datetime

def export_chores_to_csv(chore_list, filename="chore_export.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Chore", "Assigned To", "Frequency", "Next Due", "Streak", "Last Done"])
        for chore in chore_list:
            next_due = chore.get("next_due", "TBD")
            streak = chore.get("streak", 0)
            last_done = chore.get("last_done", "Never")
            writer.writerow([
                chore.get("name", ""),
                chore.get("assigned_to", ""),
                chore.get("frequency", ""),
                next_due,
                streak,
                last_done
            ])
    print(f"Exported {len(chore_list)} chores to {filename}")
    return filename
