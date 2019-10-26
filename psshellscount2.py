import csv

shell_counts = {}

for row in csv.reader(open('passwd.txt'), delimiter=':'):
    shell = row[-1]
    shell_counts[shell] = shell_counts.get(shell, 0) + 1  # add & update


for name, count in shell_counts.items():
    print(name, ':', count)
