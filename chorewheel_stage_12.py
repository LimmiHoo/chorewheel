# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ChoreWheel
def load_json_file(path, *, strict=False):
    """Load a JSON file, returning the parsed object or None on failure.
    
    If strict=True, raises ValueError with a descriptive message instead of
    silently returning None.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        if strict:
            raise ValueError(f"File not found: {path}") from None
        return None
    except json.JSONDecodeError as exc:
        if strict:
            raise ValueError(f"Malformed JSON in {path}: {exc.msg}") from exc
        return None
