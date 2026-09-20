# === Stage 57: Add structured result objects for command handlers ===
# Project: ChoreWheel
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime, timedelta


@dataclass
class CommandResult:
    """Standardized response from command handlers."""
    success: bool
    message: str
    data: Optional[dict] = None
    errors: List[str] = None

    def __post_init__(self):
        if self.errors is None:
            self.errors = []

    def to_dict(self):
        result = {"success": self.success, "message": self.message}
        if self.data is not None:
            result["data"] = self.data
        if self.errors:
            result["errors"] = self.errors
        return result


@dataclass
class ScheduleResult:
    """Result of schedule-related operations."""
    next_chore: Optional[str] = None
    next_due: Optional[datetime] = None
    streak_count: int = 0
    streak_starter: Optional[datetime] = None
    streak_break: Optional[datetime] = None
    rotation_length: int = 0
    total_assigned: int = 0


@dataclass
class ReminderResult:
    """Result of reminder operations."""
    reminders: List[dict] = None
    next_reminder: Optional[datetime] = None
    total_pending: int = 0

    def __post_init__(self):
        if self.reminders is None:
            self.reminders = []
