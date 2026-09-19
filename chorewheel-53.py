# === Stage 53: Add command help text and usage examples ===
# Project: ChoreWheel
HELP_TEXT = (
    "ChoreWheel - Household Chore Rotation Planner\n"
    "Usage:\n"
    "  chorewheel add <name> <minutes> [--days <day1,day2,...>] [--repeat <days>] [--streak <n>] [--remind <time>]\n"
    "  chorewheel list [--upcoming] [--streaks] [--reminders]\n"
    "  chorewheel remove <id>\n"
    "  chorewheel edit <id> <field>=<value>\n"
    "  chorewheel stats [--weekly] [--monthly]\n"
    "  chorewheel help\n"
    "Examples:\n"
    "  chorewheel add 'Dishes' 15 --days Mon,Wed,Fri --streak 3\n"
    "  chorewheel add 'Walk dog' 20 --days Daily --repeat 7 --remind 7:00\n"
    "  chorewheel list --upcoming\n"
    "  chorewheel stats --weekly\n"
)
