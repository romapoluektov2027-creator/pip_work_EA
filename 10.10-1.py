from math import gcd

def smallest_common_divisor(a, b):
    g = gcd(a, b)
    if g == 1:
        return 1
    d = 2
    while d * d <= g:
        if g % d == 0:
            return d
        d += 1
    return g

def reduce_fraction_steps(fraction: str) -> str:
    num, den = map(int, fraction.split('/'))
    steps = [f"{num}/{den}"]

    while True:
        d = smallest_common_divisor(num, den)
        if d == 1:
            break
        num //= d
        den //= d
        steps.append(f"{num}/{den}")

    return " = ".join(steps)


print(reduce_fraction_steps(input("введите свою дробь: ")))