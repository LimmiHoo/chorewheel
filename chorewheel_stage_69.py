# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ChoreWheel
def reset_demo_data(db):
    """Reset all tables to their demo seed data for manual testing."""
    db.execute("DELETE FROM reminders")
    db.execute("DELETE FROM streaks")
    db.execute("DELETE FROM schedules")
    db.execute("DELETE FROM assignments")
    db.execute("DELETE FROM chores")
    db.execute("DELETE FROM users")
    db.execute("DELETE FROM categories")
    db.commit()
    print("Demo data reset complete.")
