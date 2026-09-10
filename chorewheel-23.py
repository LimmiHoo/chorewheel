# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ChoreWheel
def tag_add(task, tag_name):
    if task.tags and tag_name in task.tags:
        return task
    task.tags = (task.tags or []) + [tag_name]
    return task

def tag_remove(task, tag_name):
    if not task.tags or tag_name not in task.tags:
        return task
    task.tags = [t for t in task.tags if t != tag_name]
    return task

def tag_summary(tasks):
    counts = {}
    for task in tasks:
        for tag in (task.tags or []):
            counts[tag] = counts.get(tag, 0) + 1
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)
