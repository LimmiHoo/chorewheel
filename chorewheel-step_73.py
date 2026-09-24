# === Stage 73: Add a lightweight HTML report export ===
# Project: ChoreWheel
def export_report(chore_data, filename="chore_report.html"):
    """Export a lightweight HTML report of chore assignments and streaks."""
    html = "<!DOCTYPE html><html><head><title>ChoreWheel Report</title>"
    html += "<style>body{font-family:Arial,sans-serif;margin:20px}table{border-collapse:collapse;width:100%%}th,td{border:1px solid #ddd;padding:8px;text-align:left}th{background:#f4f4f4}.streak{color:#2ecc71;font-weight:bold}</style></head><body>"
    html += "<h1>ChoreWheel Report</h1>"
    if not chore_data:
        html += "<p>No data to report.</p>"
    else:
        html += "<h2>Assignments</h2>"
        html += "<table><tr><th>Person</th><th>Chore</th><th>Days</th></tr>"
        for person, chores in chore_data.items():
            for chore, days in chores.items():
                html += f"<tr><td>{person}</td><td>{chore}</td><td>{days}</td></tr>"
        html += "</table>"
        html += "<h2>Streaks</h2>"
        for person, streaks in chore_data.get("streaks", {}).items():
            html += f"<p>{person}: {streaks}</p>"
    html += "</body></html>"
    with open(filename, "w") as f:
        f.write(html)
    return filename
