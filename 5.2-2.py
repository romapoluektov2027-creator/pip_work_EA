user_input = input("Введите целое число: ")

try:
    num = int(user_input)
    print(f"Вы ввели корректное число: {num}")
except ValueError:
    print("Ошибка: введено не целое число!")