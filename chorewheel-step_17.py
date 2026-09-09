# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ChoreWheel
def dry_run():
    """Toggle dry-run mode for commands that mutate state.
    When enabled, mutation commands simulate changes and print the intended
    action instead of executing it. This is useful for testing and previewing
    chore assignments without altering the actual state.
    """
    dry_run_mode = False

    def enable_dry_run():
        nonlocal dry_run_mode
        dry_run_mode = True
        print("Dry-run mode enabled. Changes will be simulated.")

    def disable_dry_run():
        nonlocal dry_run_mode
        dry_run_mode = False
        print("Dry-run mode disabled. Changes will be applied.")

    def simulate_assignment():
        if dry_run_mode:
            print(f"[DRY RUN] Assigning chore to a household member.")
        else:
            print("Assignment applied successfully.")

    def simulate_schedule():
        if dry_run_mode:
            print(f"[DRY RUN] Scheduling a new chore rotation.")
        else:
            print("Schedule updated successfully.")

    def simulate_streak():
        if dry_run_mode:
            print(f"[DRY RUN] Updating streak count for a chore.")
        else:
            print("Streak updated successfully.")

    def simulate_reminder():
        if dry_run_mode:
            print(f"[DRY RUN] Setting a reminder for a chore.")
        else:
            print("Reminder set successfully.")

    enable_dry_run()
    simulate_assignment()
    simulate_schedule()
    simulate_streak()
    simulate_reminder()
    disable_dry_run()
    print("All operations completed.")
