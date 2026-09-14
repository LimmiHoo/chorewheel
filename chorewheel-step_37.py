# === Stage 37: Add recommendations for the next useful action ===
# Project: ChoreWheel
def get_next_useful_action(assignment, schedule, streaks, reminders):
    """Suggest the next useful action based on current state."""
    if not reminders and not streaks:
        return "Start by setting up your first chore assignment and schedule."
    if not reminders and streaks:
        return "Set up reminders to keep track of your chore streaks."
    if not streaks and reminders:
        return "Track your streaks to stay motivated with your chore routine."
    if not reminders and not streaks and not schedule:
        return "Create a schedule to organize when each chore should be done."
    return "Review your progress and adjust your schedule as needed."
