# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ChoreWheel
def snapshot_diff(before, after, keys=("id", "name", "status", "created_at")):
    """Return a dict of fields where before and after differ."""
    return {k: (after.get(k), before.get(k)) for k in keys if after.get(k) != before.get(k)}
