matrix = [
    [11, 32, 13, 44, 55],
    [31, 42, 53, 66, 75],
    [12, 26, 33, 45, 52],
    [15, 22, 35, 64, 57],
    [21, 52, 32, 44, 38],
]

max_i = max_j = min_i = min_j = 0
for i, row in enumerate(matrix):
    for j, x in enumerate(row):
        if x > matrix[max_i][max_j]:
            max_i, max_j = i, j
        if x < matrix[min_i][min_j]:
            min_i, min_j = i, j

print(f"Максимум: {matrix[max_i][max_j]} в позиции ({max_i}, {max_j})")
print(f"Минимум:  {matrix[min_i][min_j]} в позиции ({min_i}, {min_j})")

matrix[max_i][max_j], matrix[min_i][min_j] = matrix[min_i][min_j], matrix[max_i][max_j]

for row in matrix:
    print(row)