# === Stage 46: Add a schema version field and migration helper ===
# Project: ChoreWheel
import json
import sqlite3
import os

SCHEMA_VERSION = 3

def migrate_chorewheel(db_path: str = "chorewheel.db") -> None:
    """Apply schema migrations for ChoreWheel and log each step."""
    with open(os.path.join(os.path.dirname(__file__), "schema_history.json")) as f:
        history = json.load(f)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS schema_history (version INTEGER PRIMARY KEY, applied_at TEXT)")
    c.execute("SELECT COUNT(*) FROM schema_history")
    if c.fetchone()[0] == 0:
        conn.commit()

    for version, sql in history.items():
        c.execute(f"ALTER TABLE chore_assignments ADD COLUMN {sql}")
        c.execute("DELETE FROM schema_history WHERE version = ?", (version,))
    conn.commit()
    conn.close()
