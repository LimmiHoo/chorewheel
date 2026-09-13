# === Stage 32: Add pagination helpers for long console output ===
# Project: ChoreWheel
def paginate(text, chunk_size=80):
    """Yield text in chunks of `chunk_size` characters."""
    for i in range(0, len(text), chunk_size):
        yield text[i:i+chunk_size]

def print_paged(text, chunk_size=80):
    """Print text in paged chunks with a progress indicator."""
    chunks = list(paginate(text, chunk_size))
    for idx, chunk in enumerate(chunks, 1):
        print(chunk, end="")
        if idx < len(chunks):
            print()
            print(f"{'='*chunk_size}")
    print("\n[DONE]")

def paged_list(items, chunk_size=10):
    """Print a list of items in paged chunks, numbered within each page."""
    for page_num in range(0, len(items), chunk_size):
        page = items[page_num:page_num+chunk_size]
        for idx, item in enumerate(page, 1):
            print(f"  [{page_num // chunk_size + 1}/{(len(items) + chunk_size - 1) // chunk_size}] {idx}. {item}")
        if page_num + chunk_size < len(items):
            print()
    print("[END]")
