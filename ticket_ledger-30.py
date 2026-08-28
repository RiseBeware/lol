# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: TicketLedger
class Profile:
    def __init__(self, name, role="user", is_admin=False):
        self.name = name
        self.role = role
        self.is_admin = is_admin

    def __repr__(self):
        return f"Profile(name={self.name!r}, role={self.role!r}, is_admin={self.is_admin})"


class ProfileManager:
    def __init__(self):
        self.profiles = {}

    def add(self, name, role="user", is_admin=False):
        self.profiles[name] = Profile(name, role, is_admin)
        return self.profiles[name]

    def remove(self, name):
        return self.profiles.pop(name, None)

    def get(self, name):
        return self.profiles.get(name)

    def list_all(self):
        return list(self.profiles.values())

    def has_admin(self):
        return any(p.is_admin for p in self.profiles.values())

    def __repr__(self):
        return f"ProfileManager(count={len(self.profiles)})"


# пример использования
if __name__ == "__main__":
    pm = ProfileManager()
    pm.add("admin", role="admin", is_admin=True)
    pm.add("user1", role="user")
    pm.add("user2", role="user")
    print(pm.list_all())
    print(pm.has_admin())
    print(pm.get("user1"))
    pm.remove("user2")
    print(pm.list_all())
