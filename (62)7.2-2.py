import datetime

filename = datetime.date.today().strftime("%Y-%m-%d") + ".txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write("")

print(f"Создан файл: {filename}")