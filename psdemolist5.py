"""delete by value"""

items = ['sam', 3.3, 'pam', 2.2, .98, 'peter', .34, 1.2, 'penny', 4, 'patric', 3]
temp = []

for item in items:
    if type(item) is str:  # identity operator is, is not
        if item.startswith('p'):
            continue

    temp.append(item)

print(temp)
