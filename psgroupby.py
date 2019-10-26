import csv
# import pprint

group_by = {}

for row in csv.reader(open('passwd.txt'), delimiter=':'):
    user, shell = row[0], row[-1]

    if shell not in group_by:
        group_by[shell] = []

    group_by[shell].append(user)

# pprint.pprint(group_by)

for shell_name, list_of_users in group_by.items():
    print(shell_name)

    for user in list_of_users:
        print(f'\t{user}')  # formatted string

    print()
