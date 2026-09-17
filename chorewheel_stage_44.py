# === Stage 44: Add backup creation for the data file ===
# Project: ChoreWheel
def create_backup(source_path, backup_dir="."):
    """Create a timestamped backup of the chore data file."""
    import shutil
    import os
    from datetime import datetime

    if not os.path.exists(source_path):
        print(f"Source file not found: {source_path}")
        return False

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"chorewheel_backup_{timestamp}.json")

    try:
        shutil.copy2(source_path, backup_path)
        print(f"Backup created: {backup_path}")
        return True
    except Exception as e:
        print(f"Backup failed: {e}")
        return False
