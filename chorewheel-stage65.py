# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ChoreWheel
import re

def merge_imports(source, target):
    """Append `source` imports to `target`, skipping lines whose stripped content
    is identical (case-insensitive) to any already present in `target`."""
    existing = set()
    for line in target.splitlines():
        stripped = line.strip().lower()
        if stripped.startswith("import") or stripped.startswith("from"):
            existing.add(stripped)

    result = list(target.splitlines())
    for line in source.splitlines():
        stripped = line.strip().lower()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped in existing:
            continue
        existing.add(stripped)
        result.append(line)

    return "\n".join(result)
