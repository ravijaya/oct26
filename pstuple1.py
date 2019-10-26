"""tuple
        - immutable object
        - readonly list
"""

items = (2.2, 1.3, 2, 'kim', 'pam', 'jane', 'jack', 4+2j)
print(items)
print(type(items))
print(len(items))
print()

print(items[-4])  # indexing
print()
print(items[-4:])  # slicing


for item in items[-4:]:  # iterate
    print(item)