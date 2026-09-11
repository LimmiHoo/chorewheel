# === Stage 25: Add daily summary calculations ===
# Project: ChoreWheel
def daily_summary(chore_log):
    """Compute a compact daily summary from the chore log.

    Args:
        chore_log: dict mapping date strings to lists of completed chores.

    Returns:
        dict with keys 'completed', 'total', 'average', 'most_common'.
    """
    completed = sum(len(chores) for chores in chore_log.values())
    days = len(chore_log) if chore_log else 0
    average = completed / days if days else 0.0

    if completed:
        flat = [chore for chores in chore_log.values() for chore in chores]
        from collections import Counter
        most_common = Counter(flat).most_common(1)[0][0]
    else:
        most_common = None

    return {
        'completed': completed,
        'total': completed,
        'average': average,
        'most_common': most_common,
    }
