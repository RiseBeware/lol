# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: TicketLedger
def switch_profile(profile_name):
    profiles = {
        "admin": {"name": "Администратор", "role": "admin", "tickets": []},
        "analyst": {"name": "Аналитик", "role": "analyst", "tickets": []},
        "manager": {"name": "Менеджер", "role": "manager", "tickets": []},
    }
    if profile_name in profiles:
        active_user = profiles[profile_name]
        active_user["name"] = profile_name
        active_user["role"] = profile_name
        active_user["tickets"] = []
        return active_user
    else:
        raise ValueError(f"Неизвестный профиль: {profile_name}")
