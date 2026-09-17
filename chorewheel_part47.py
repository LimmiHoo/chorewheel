# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ChoreWheel
def main():
    from chorewheel import ChoreWheel

    cw = ChoreWheel()
    cw.add_person("Alice")
    cw.add_person("Bob")
    cw.add_person("Charlie")

    cw.add_schedule("Monday", ["Dishes", "Vacuum"])
    cw.add_schedule("Tuesday", ["Laundry", "Sweep"])
    cw.add_schedule("Wednesday", ["Dishes", "Dust"])
    cw.add_schedule("Thursday", ["Laundry", "Vacuum"])
    cw.add_schedule("Friday", ["Sweep", "Dishes"])
    cw.add_schedule("Saturday", ["Garden", "Laundry"])
    cw.add_schedule("Sunday", ["Dishes", "Sweep"])

    cw.add_assignment("Alice", "Monday", "Dishes")
    cw.add_assignment("Bob", "Monday", "Vacuum")
    cw.add_assignment("Charlie", "Tuesday", "Laundry")

    cw.complete_assignment("Alice", "Monday", "Dishes")
    cw.complete_assignment("Bob", "Monday", "Vacuum")
    cw.complete_assignment("Charlie", "Tuesday", "Laundry")

    cw.add_reminder("Monday 8:00am")
    cw.add_reminder("Tuesday 9:00am")

    print(cw.get_schedule())
    print(cw.get_assignments())
    print(cw.get_streaks())
    print(cw.get_reminders())

main()
