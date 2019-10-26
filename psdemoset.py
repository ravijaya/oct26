items = {'pam', 'eva', 'andy', 'pam'}  # set()

# set aka unordered collection
# unique
print(items)
print()

items.add('nickson')
items.add('nickson')
# items.add(.98)
print(items)
print()

items.remove('pam')  # delete
print(items)
print()

# iterate

for item in items:
    print(item)
