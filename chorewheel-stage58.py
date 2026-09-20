# === Stage 58: Add bulk update behavior for selected records ===
# Project: ChoreWheel
import json
import csv
from pathlib import Path

def bulk_update_assignments(csv_path, assignments):
    """Update multiple chore assignments at once.
    
    Args:
        csv_path: Path to the assignments CSV file.
        assignments: List of dictionaries with keys 'id', 'name', 'status'.
        
    Returns:
        Number of rows updated.
    """
    if not assignments:
        return 0

    records = []
    with open(csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    updated_count = 0
    for assignment in assignments:
        for record in records:
            if record['id'] == assignment['id']:
                record['name'] = assignment['name']
                record['status'] = assignment['status']
                updated_count += 1

    with open(csv_path, 'w', newline='') as f:
        fieldnames = ['id', 'name', 'status']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    return updated_count
