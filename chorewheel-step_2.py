# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ChoreWheel
from dataclasses import dataclass, field
from datetime import date

@dataclass
class ChoreAssignment:
    name: str
    assigned_to: str
    due_date: date
    completed: bool = False
    streak: int = 0
    notes: str = ""
