# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ChoreWheel
def archive_record(record: dict) -> None:
    if record.get("status") in ("done", "skipped", "missed"):
        record["archived"] = True
        record["archived_at"] = datetime.now().isoformat()
        record["completed_at"] = record.get("completed_at") or datetime.fromisoformat(
            record.get("completed_at", "")
        ).isoformat()
    if record.get("archived"):
        record["archive_note"] = (
            f"Completed on {record['completed_at']}"
            if record.get("completed_at")
            else "Skipped or missed"
        )
