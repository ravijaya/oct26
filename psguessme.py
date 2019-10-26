import random

chance = 1
max_chance = 10
rand_value = random.randint(1, 1000)

while chance <= max_chance:
    try:
        print('Chance :', chance)
        user_value = int(input('enter the value :'))
    except ValueError as err:
        print('invalid input, retrying......\n')
        continue

    if user_value == rand_value:
        print('you won :) !!!!!!!!')
        break
    elif user_value < rand_value:
        print(user_value, ': lesser')
    else:
        print(user_value, ': greater')

    chance += 1
    print()
else:
    print('you lost :(............')
