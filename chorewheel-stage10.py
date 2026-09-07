# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ChoreWheel
class ChoreWheel:
    def __init__(self):
        self.assignments = []
        self.reminders = []

    def add_assignment(self, name, person, frequency, interval=7, streak=0, streak_max=7, next_run=None):
        self.assignments.append({'name': name, 'person': person, 'frequency': frequency, 'interval': interval, 'streak': streak, 'streak_max': streak_max, 'next_run': next_run})
        return self

    def add_reminder(self, message, time, due_date):
        self.reminders.append({'message': message, 'time': time, 'due_date': due_date})
        return self

    def search(self, query):
        query = query.lower()
        results = []
        for a in self.assignments:
            if (query in a['name'].lower() or query in a['person'].lower() or query in a['frequency'].lower()) and a['next_run'] is None:
                results.append(a)
        for r in self.reminders:
            if query in r['message'].lower():
                results.append(r)
        return results

    def get_due(self):
        now = datetime.now()
        due = []
        for r in self.reminders:
            if r['due_date'] <= now:
                due.append(r)
        return due

    def get_overdue(self):
        now = datetime.now()
        overdue = []
        for a in self.assignments:
            if a['next_run'] is not None and a['next_run'] <= now:
                overdue.append(a)
        return overdue

    def get_reminders_sorted(self):
        sorted_reminders = sorted(self.reminders, key=lambda x: x['due_date'])
        return sorted_reminders

    def get_assignments_sorted(self):
        sorted_assignments = sorted(self.assignments, key=lambda x: x['next_run'])
        return sorted_assignments

    def get_streaks(self):
        streaks = []
        for a in self.assignments:
            if a['next_run'] is not None and a['next_run'] <= datetime.now():
                streaks.append(a)
        return streaks
