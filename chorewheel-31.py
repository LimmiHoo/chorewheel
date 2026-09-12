# === Stage 31: Add compact table rendering for long lists ===
# Project: ChoreWheel
def render_compact_table(rows, headers=None, max_width=80):
    """Render a compact text table from a list of row dicts."""
    if not rows:
        return ""
    cols = list(rows[0].keys())
    if headers is None:
        headers = cols
    widths = {h: len(str(h)) for h in headers}
    for row in rows:
        for col in cols:
            v = str(row.get(col, ""))
            widths[col] = max(widths[col], len(v))
    widths = {k: min(v, max_width) for k, v in widths.items()}
    lines = []
    lines.append("│" + "│".join(str(h).ljust(widths[h]) for h in headers) + "│")
    sep = "─" * widths[cols[0]]
    lines.append("├" + "┼".join(sep for _ in cols) + "┤")
    for row in rows:
        line = "│" + "│".join(str(row.get(c, "")).ljust(widths[c]) for c in cols) + "│"
        lines.append(line)
    return "\n".join(lines)
