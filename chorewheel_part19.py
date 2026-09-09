# === Stage 19: Add undo support for the last simple mutation ===
# Project: ChoreWheel
def undo(self):
        if self._undo_stack:
            action, state = self._undo_stack.pop()
            self._state = state
            self._notify(action, reverse=True)
