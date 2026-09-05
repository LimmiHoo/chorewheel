# === Stage 4: Implement create operations for the primary records ===
# Project: ChoreWheel
def create_chore(chore_data):
    """Create a new chore record."""
    chore_id = generate_id()
    chore = {
        'id': chore_id,
        'name': chore_data['name'],
        'category': chore_data.get('category', 'General'),
        'estimated_minutes': chore_data.get('estimated_minutes', 30),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    chores.append(chore)
    return chore


def create_assignee(assignee_data):
    """Create a new assignee record."""
    assignee_id = generate_id()
    assignee = {
        'id': assignee_id,
        'name': assignee_data['name'],
        'email': assignee_data.get('email', ''),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    assignees.append(assignee)
    return assignee


def create_schedule(schedule_data):
    """Create a new schedule record."""
    schedule_id = generate_id()
    schedule = {
        'id': schedule_id,
        'chore_id': schedule_data['chore_id'],
        'assignee_id': schedule_data['assignee_id'],
        'start_date': schedule_data['start_date'],
        'end_date': schedule_data.get('end_date', None),
        'recurring': schedule_data.get('recurring', False),
        'frequency': schedule_data.get('frequency', 'weekly'),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    schedules.append(schedule)
    return schedule
