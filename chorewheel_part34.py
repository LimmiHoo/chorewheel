# === Stage 34: Add support for multiple local user profiles ===
# Project: ChoreWheel
import json

class ProfileManager:
    def __init__(self, profiles_path="profiles.json"):
        self.profiles_path = profiles_path
        self.profiles = self._load_profiles()

    def _load_profiles(self):
        try:
            with open(self.profiles_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"profiles": [], "active_profile": 0}

    def add_profile(self, name, email=None, phone=None):
        self.profiles["profiles"].append({"name": name, "email": email, "phone": phone})
        self.save()

    def remove_profile(self, name):
        self.profiles["profiles"] = [p for p in self.profiles["profiles"] if p["name"] != name]
        if self.profiles["active_profile"] >= len(self.profiles["profiles"]):
            self.profiles["active_profile"] = max(0, len(self.profiles["profiles"]) - 1)
        self.save()

    def switch_profile(self, name):
        for i, p in enumerate(self.profiles["profiles"]):
            if p["name"] == name:
                self.profiles["active_profile"] = i
                self.save()
                return True
        return False

    def get_active_profile(self):
        return self.profiles["profiles"][self.profiles["active_profile"]] if self.profiles["profiles"] else None

    def save(self):
        with open(self.profiles_path, "w") as f:
            json.dump(self.profiles, f, indent=2)
