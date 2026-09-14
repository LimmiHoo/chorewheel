# === Stage 36: Add templates for quickly creating common records ===
# Project: ChoreWheel
class ChoreTemplates:
    """Compact templates for quickly creating common chore records."""

    @staticmethod
    def daily_cleaning_schedule():
        return {
            "template_name": "Daily Cleaning",
            "assignments": [
                {"chore": "Dusting", "location": "Living Room", "duration_min": 15},
                {"chore": "Wiping Counters", "location": "Kitchen", "duration_min": 10},
                {"chore": "Vacuuming", "location": "Hallway", "duration_min": 15},
            ],
            "schedule_type": "daily",
            "time": "18:00",
        }

    @staticmethod
    def weekly_deep_clean():
        return {
            "template_name": "Weekly Deep Clean",
            "assignments": [
                {"chore": "Mopping Floors", "location": "Entire House", "duration_min": 30},
                {"chore": "Cleaning Bathrooms", "location": "All Bathrooms", "duration_min": 45},
                {"chore": "Changing Sheets", "location": "Bedrooms", "duration_min": 20},
            ],
            "schedule_type": "weekly",
            "day": "Sunday",
            "time": "09:00",
        }

    @staticmethod
    def monthly_maintenance():
        return {
            "template_name": "Monthly Maintenance",
            "assignments": [
                {"chore": "Cleaning Fridge", "location": "Kitchen", "duration_min": 20},
                {"chore": "Washing Oven", "location": "Kitchen", "duration_min": 30},
                {"chore": "Dusting Blinds", "location": "Windows", "duration_min": 25},
            ],
            "schedule_type": "monthly",
            "day": 1,
            "month": "January",
            "time": "10:00",
        }

    @staticmethod
    def quick_streak_reminder():
        return {
            "reminder_type": "streak_check",
            "message_template": "Great job! You've completed {count} days in a row. Keep it up!",
            "trigger": "after_completion",
            "interval_days": 1,
        }
