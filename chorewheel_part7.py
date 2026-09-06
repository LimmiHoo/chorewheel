# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ChoreWheel
def format_chore(chore: Chore) -> str:
    return f"[{chore.owner}] {chore.title} (next: {chore.next_date}, streak: {chore.streak})"

def format_schedule(schedule: Schedule) -> str:
    lines = [f"Schedule: {schedule.name}\n"]
    for day, chores in schedule.assigned.items():
        lines.append(f"  {day}: {', '.join(format_chore(c) for c in chores)}")
    return "\n".join(lines)

def format_summary(schedules: dict[str, Schedule]) -> str:
    result = "ChoreWheel Summary:\n"
    for name, sched in schedules.items():
        result += format_schedule(sched) + "\n"
    return result
