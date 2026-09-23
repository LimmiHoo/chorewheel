# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ChoreWheel
def build_changelog(activity_log):
    """Generate a compact human-readable changelog from the activity log."""
    if not activity_log:
        return "No activities recorded."
    
    lines = []
    lines.append("=== ChoreWheel Changelog ===")
    lines.append("")
    
    seen = set()
    for entry in activity_log:
        date = entry.get("date", "unknown")
        if date in seen:
            continue
        seen.add(date)
        event = entry.get("event", "unknown")
        lines.append(f"- {date}: {event}")
    
    return "\n".join(lines)
