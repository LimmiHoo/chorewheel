# === Stage 16: Add argparse support for the most common commands ===
# Project: ChoreWheel
import argparse

def register_subparsers(parser):
    sub = parser.add_subparsers(dest="command")

    # chore
    p = sub.add_parser("chore", help="manage chores")
    p_sub = p.add_subparsers(dest="action")
    p_new = p_sub.add_parser("new", help="add a new chore")
    p_new.add_argument("--name", required=True, help="chore name")
    p_new.add_argument("--assignee", help="person assigned")
    p_show = p_sub.add_parser("show", help="list all chores")
    p_done = p_sub.add_parser("done", help="mark a chore done")
    p_done.add_argument("name", help="chore to mark done")

    # schedule
    p = sub.add_parser("schedule", help="manage schedules")
    p_sub = p.add_subparsers(dest="action")
    p_show = p_sub.add_parser("show", help="list all schedules")
    p_now = p_sub.add_parser("now", help="show next scheduled task")

    # streak
    p = sub.add_parser("streak", help="manage streaks")
    p_show = p.add_parser("show", help="show all streaks")

    # reminder
    p = sub.add_parser("reminder", help="set reminders")
    p_show = p.add_parser("show", help="list all reminders")
    p_next = p.add_parser("next", help="show next reminder")

    return parser
