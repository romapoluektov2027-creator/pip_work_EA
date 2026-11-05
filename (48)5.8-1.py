import datetime

# Запрашиваем год с проверкой
while True:
    try:
        year = int(input("Введите год: "))
        break
    except ValueError:
        print("Ошибка: введите целое число!")

# Перебираем все месяцы года
fridays_13 = []
for month in range(1, 13):
    date = datetime.date(year, month, 13)
    if date.weekday() == 4:   # 4 = пятница (0=пн, 1=вт, ..., 4=пт, 5=сб, 6=вс)
        fridays_13.append(date)

print(f"Пятницы 13-е в {year} году:")
for d in fridays_13:
    print(d.strftime("%d.%m.%Y (%A)"))