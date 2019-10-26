import csv

shell_counts = {}
fp = open('passwd.txt')

for row in csv.reader(fp , delimiter=':'):
    shell = row[-1]

    if shell in shell_counts:
        shell_counts[shell] += 1
    else:
        shell_counts[shell] = 1

fp.close()
for name, count in shell_counts.items():
    print(name, ':', count)
