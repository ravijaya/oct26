name, age, = 'sarah', 3
print('I am name, age years old')
print()
print(f'I am {name}, {age} years old')  # formatted string
print()

content = f'I am {name.title()}, {age * 3} years old'
print(content)
open('dat.pdf', 'a').write(content+'\n')
