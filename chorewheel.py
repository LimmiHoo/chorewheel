# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ChoreWheel
import random

HOUSES = [
    {
        "id": 1,
        "name": "The Smiths",
        "members": [
            {"id": 1, "name": "Alice", "age": 32},
            {"id": 2, "name": "Bob", "age": 35},
            {"id": 3, "name": "Charlie", "age": 7},
        ],
    },
    {
        "id": 2,
        "name": "The Johnsons",
        "members": [
            {"id": 1, "name": "Diana", "age": 28},
            {"id": 2, "name": "Ethan", "age": 30},
            {"id": 3, "name": "Fiona", "age": 5},
        ],
    },
]

CHORES = [
    "Dishes", "Sweeping", "Vacuuming", "Bed making", "Trash",
    "Laundry", "Dusting", "Watering plants", "Pet feeding", "Grocery shopping",
]

STREAKS = {
    "Dishes": {"members": {"Alice": 12, "Bob": 5}, "house_id": 1},
    "Sweeping": {"members": {"Ethan": 3, "Fiona": 0}, "house_id": 2},
}

SCHEDULES = {
    1: {"Dishes": "Alice", "Sweeping": "Bob", "Vacuuming": "Charlie"},
    2: {"Sweeping": "Ethan", "Watering plants": "Fiona", "Pet feeding": "Diana"},
}
