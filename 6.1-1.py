import datetime

def current_weekday():
    """Возвращает текущий день недели по-русски."""
    days = ["понедельник", "вторник", "среда",
            "четверг", "пятница", "суббота", "воскресенье"]
    return days[datetime.date.today().weekday()]

print(current_weekday())