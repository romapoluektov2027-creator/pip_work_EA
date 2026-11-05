num = 12345

result = all(int(d) > 0 for d in str(num))
print(result)