items = [1, 3, 2, 4, 5]

t = [item ** 2 for item in items]  # list comprehension
print(t)

print()

t = [[hex(i), oct(i), bin(i)] for i in items]  # list comprehension
print(t)
