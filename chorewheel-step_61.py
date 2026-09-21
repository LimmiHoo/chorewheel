# === Stage 61: Add performance timing for core list and search operations ===
# Project: ChoreWheel
import time
from collections import defaultdict

class PerformanceTracker:
    def __init__(self):
        self.timings = defaultdict(list)

    def measure(self, func, *args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        self.timings[func.__name__].append(elapsed)
        return result

    def report(self, func_name, n=10):
        data = self.timings.get(func_name, [])
        if not data:
            return f"{func_name}: no measurements"
        data.sort()
        avg = sum(data) / len(data)
        p50 = data[len(data) // 2]
        p95 = data[int(len(data) * 0.95)]
        return f"{func_name}: avg={avg:.4f}s p50={p50:.4f}s p95={p95:.4f}s (n={len(data)})"

    def reset(self):
        self.timings.clear()
