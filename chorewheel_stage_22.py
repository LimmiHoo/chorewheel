# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ChoreWheel
class Favorite:
    def __init__(self, assignment_id, created_at=None):
        self.assignment_id = assignment_id
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {"assignment_id": self.assignment_id, "created_at": self.created_at.isoformat()}

    @classmethod
    def from_dict(cls, data):
        return cls(assignment_id=data["assignment_id"], created_at=datetime.fromisoformat(data["created_at"]))

    def __repr__(self):
        return f"Favorite(assignment_id={self.assignment_id})"

class FavoriteRepository:
    def __init__(self):
        self._favorites = []

    def add(self, assignment_id):
        if not self._is_favorite(assignment_id):
            self._favorites.append(Favorite(assignment_id))

    def _is_favorite(self, assignment_id):
        return any(f.assignment_id == assignment_id for f in self._favorites)

    def is_favorite(self, assignment_id):
        return self._is_favorite(assignment_id)

    def get_favorites(self):
        return [f.assignment_id for f in self._favorites]

    def clear(self):
        self._favorites.clear()
