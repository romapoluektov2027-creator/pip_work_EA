def prime_factors(n):
    """Возвращает список простых множителей числа n."""
    n = abs(n)
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
    return factors

# Ввод с проверкой
while True:
    try:
        num = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Ошибка: введите целое число!")

if num == 0:
    print("Ноль не имеет разложения на простые множители.")
elif abs(num) == 1:
    print("Единица не является простым числом и не раскладывается.")
else:
    factors = prime_factors(num)
    print(f"{num} = " + " × ".join(map(str, factors)))