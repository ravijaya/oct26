"""delete by value"""

items = [3.3, 'pam', 2.2, .98, 'peter', .34, 1.2, 'pam', 4, 'pam', 3]
print('lists :', items)
print()

item = 'pam'
print(item in items)  # list contains 'pam'
print()

while item in items:   # membership test operator in, not in
    items.remove(item)

print(items)
print()

