# === Stage 56: Add compact error classes for domain failures ===
# Project: ChoreWheel
class ChoreWheelError(Exception):
    """Base error for ChoreWheel domain failures."""
    pass


class InvalidChoreError(ChoreWheelError):
    """Raised when a chore definition is malformed."""
    pass


class ScheduleConflictError(ChoreWheelError):
    """Raised when two assignments overlap or miss a scheduled slot."""
    pass


class StreakResetError(ChoreWheelError):
    """Raised when a streak cannot be updated (e.g., invalid date)."""
    pass


class ReminderError(ChoreWheelError):
    """Raised when a reminder cannot be created or fired."""
    pass


class RotationError(ChoreWheelError):
    """Raised when the rotation cycle is broken or incomplete."""
    pass
