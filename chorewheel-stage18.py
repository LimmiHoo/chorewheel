# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ChoreWheel
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action: str, chore_name: str, user: str, time: str = None):
        entry = {
            "action": action,
            "chore": chore_name,
            "user": user,
            "timestamp": time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.entries.append(entry)
        return entry
