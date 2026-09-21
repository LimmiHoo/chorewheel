# === Stage 60: Add saved views for frequently used filters ===
# Project: ChoreWheel
class SavedView:
    def __init__(self, name, filters=None, sort=None, limit=None):
        self.name = name
        self.filters = filters or {}
        self.sort = sort or None
        self.limit = limit
        self.active = True

    def apply(self, chore_list):
        filtered = chore_list
        for key, value in self.filters.items():
            if isinstance(value, str):
                filtered = [c for c in filtered if getattr(c, key) == value]
            else:
                filtered = [c for c in filtered if getattr(c, key) in value]
        if self.sort:
            filtered = sorted(filtered, key=self.sort)
        if self.limit:
            filtered = filtered[:self.limit]
        return filtered

    def to_dict(self):
        return {
            'name': self.name,
            'filters': self.filters,
            'sort': self.sort,
            'limit': self.limit,
            'active': self.active,
        }

    def from_dict(cls, data):
        self = cls.__new__(cls)
        self.name = data['name']
        self.filters = data.get('filters', {})
        self.sort = data.get('sort')
        self.limit = data.get('limit')
        self.active = data.get('active', True)
        return self
