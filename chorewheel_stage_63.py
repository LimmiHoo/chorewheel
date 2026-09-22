# === Stage 63: Add relationships between records where useful ===
# Project: ChoreWheel
@dataclass
class ChoreAssignment:
    chore_id: int
    user_id: int
    scheduled_date: date
    completed: bool = False
    streak: int = 0
    last_completed: Optional[date] = None

    def mark_complete(self, today: date) -> None:
        self.completed = True
        self.last_completed = today
        if self.streak:
            self.streak += 1
        else:
            self.streak = 1

    def mark_miss(self, today: date) -> None:
        self.completed = False
        if self.last_completed:
            delta = (today - self.last_completed).days
            if delta == 1:
                self.streak = 0
            else:
                self.streak = max(0, self.streak - 1)
        else:
            self.streak = 0
