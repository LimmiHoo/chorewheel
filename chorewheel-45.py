# === Stage 45: Add restore from backup with validation ===
# Project: ChoreWheel
import json, os
from datetime import datetime

BACKUP_DIR = "backups"

def _ensure_backup_dir():
    os.makedirs(BACKUP_DIR, exist_ok=True)

def restore_backup(backup_path):
    _ensure_backup_dir()
    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f"Backup file not found: {backup_path}")
    with open(backup_path, "r") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Invalid backup format: expected a JSON object")
    required_keys = {"assignments", "schedules", "streaks", "last_sync"}
    missing = required_keys - set(data.keys())
    if missing:
        raise ValueError(f"Backup is missing required keys: {missing}")
    assignments = {k: v for k, v in data["assignments"].items() if isinstance(v, dict)}
    schedules = {k: v for k, v in data["schedules"].items() if isinstance(v, dict)}
    streaks = {k: v for k, v in data["streaks"].items() if isinstance(v, dict)}
    _last_sync = datetime.strptime(data["last_sync"], "%Y-%m-%d %H:%M:%S")
    if _last_sync > datetime.utcnow():
        raise ValueError("Backup timestamp is in the future; refusing to restore")
    _current = {
        "assignments": assignments,
        "schedules": schedules,
        "streaks": streaks,
        "last_sync": _last_sync.strftime("%Y-%m-%d %H:%M:%S"),
    }
    return _current
