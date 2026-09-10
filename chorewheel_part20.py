# === Stage 20: Add duplicate detection for newly created records ===
# Project: ChoreWheel
def find_duplicate(self, record):
    """Return the existing record with the same unique key, or None."""
    key = self._make_unique_key(record)
    for existing in self._records:
        if self._make_unique_key(existing) == key:
            return existing
    return None
