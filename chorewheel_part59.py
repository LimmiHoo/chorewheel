# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ChoreWheel
def bulk_delete(chore_assignments: list, confirm: bool) -> list:
    if not confirm:
        raise ValueError("Bulk delete requires explicit confirmation (confirm=True).")
    remaining = []
    for assignment in chore_assignments:
        assignment["deleted"] = True
        remaining.append(assignment)
    return remaining
