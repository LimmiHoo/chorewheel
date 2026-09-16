# === Stage 43: Add CSV import for the primary record type ===
# Project: ChoreWheel
def import_chores_csv(file_path):
    """Import chore assignments from a CSV file."""
    import csv
    chores = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            chores.append({
                'name': row['name'],
                'assignee': row['assignee'],
                'frequency': row.get('frequency', 'weekly'),
                'day': row.get('day', 'any'),
                'completed': False,
                'streak': 0,
            })
    return chores
