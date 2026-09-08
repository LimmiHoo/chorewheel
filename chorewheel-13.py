# === Stage 13: Add file save support using a configurable path ===
# Project: ChoreWheel
import json, os, sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def get_storage_path():
    path = os.environ.get("CHOREWHEEL_STORAGE", "")
    if not path:
        path = os.path.join(PROJECT_ROOT, "data", "chorewheels.json")
    return os.path.abspath(path)

def save_chorewheels(chorewheels):
    storage_path = get_storage_path()
    os.makedirs(os.path.dirname(storage_path), exist_ok=True)
    with open(storage_path, "w", encoding="utf-8") as f:
        json.dump(chorewheels, f, indent=2)

def load_chorewheels():
    storage_path = get_storage_path()
    if not os.path.exists(storage_path):
        return []
    with open(storage_path, "r", encoding="utf-8") as f:
        return json.load(f)
