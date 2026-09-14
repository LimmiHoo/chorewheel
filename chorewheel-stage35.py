# === Stage 35: Add active user switching and user-specific records ===
# Project: ChoreWheel
class User:
    def __init__(self, name, email=""):
        self.name = name
        self.email = email
        self.streak = 0
        self.last_active_date = None

    def mark_active(self, date):
        self.last_active_date = date
        if self.last_active_date == date:
            self.streak += 1
        else:
            self.streak = 1

    def __repr__(self):
        return f"<User {self.name} (streak={self.streak})>"
