import datetime

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_to_next_feb29(today=None):
    """Сколько дней осталось до ближайшего 29 февраля."""
    if today is None:
        today = datetime.date.today()

    year = today.year
    while True:
        if is_leap(year):
            target = datetime.date(year, 2, 29)
            if target >= today:
                return (target - today).days
        year += 1

print(days_to_next_feb29())