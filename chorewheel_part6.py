# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ChoreWheel
def remove_assignment(chore_id: int) -> bool:
    """Remove a chore assignment by its ID. Returns True if removed, False otherwise."""
    if chore_id in chore_assignments:
        del chore_assignments[chore_id]
        print(f"Assignment {chore_id} removed.")
        return True
    print(f"Assignment {chore_id} not found.")
    return False
