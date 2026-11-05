import random

matrix = [
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33],
]

for row in matrix:
    row.append(random.randint(1, 99))

for row in matrix:
    print(row)