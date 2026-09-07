# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ChoreWheel
def filter_chores(chores, status=None, category=None, owner=None, tag=None):
    result = []
    for c in chores:
        if status is not None and c.get('status') != status:
            continue
        if category is not None and c.get('category') != category:
            continue
        if owner is not None and c.get('owner') != owner:
            continue
        if tag is not None and tag not in c.get('tags', []):
            continue
        result.append(c)
    return result
