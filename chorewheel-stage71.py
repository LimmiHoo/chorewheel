# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ChoreWheel
def seed_demo_data():
    """Populate ChoreWheel with deterministic sample data for quick testing."""
    from chorewheels.domain.models import (
        Assignment, Schedule, Streak, Reminder,
        AssignmentStatus, DayOfWeek, ReminderType
    )
    from chorewheels.domain.services import AssignmentService, ScheduleService, StreakService, ReminderService
    import datetime

    assignments = [
        Assignment("Dishes", "Kitchen", AssignmentStatus.COMPLETED),
        Assignment("Laundry", "Laundry Room", AssignmentStatus.PENDING),
        Assignment("Vacuum", "Living Room", AssignmentStatus.IN_PROGRESS),
        Assignment("Dusting", "Bedroom", AssignmentStatus.COMPLETED),
    ]
    service = AssignmentService()
    for a in assignments:
        service.create(a)

    schedule = Schedule(
        day_of_week=DayOfWeek.MONDAY,
        start_time=datetime.time(10, 0),
        duration=datetime.timedelta(minutes=30)
    )
    service2 = ScheduleService()
    service2.create(schedule)

    streak = Streak("Dishes", 5)
    service3 = StreakService()
    service3.create(streak)

    reminder = Reminder(
        message="Don't forget to do Dishes after dinner!",
        type=ReminderType.EMAIL,
        schedule=ScheduleType.DAILY,
        day_of_week=DayOfWeek.MONDAY,
        time=datetime.time(20, 0)
    )
    service4 = ReminderService()
    service4.create(reminder)

    return {
        "assignments": assignments,
        "schedule": schedule,
        "streak": streak,
        "reminder": reminder
    }
