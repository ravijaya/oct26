a = [1, 2, 3, 4, 5]
b = [1, 3, 5, 7, 9]

x = set(a)
y = set(b)
print(list(x.intersection(y)))
print(x & y)

print()
print(x.union(y))
print(x | y)

print()
print(x.difference(y))
print(y - x)
