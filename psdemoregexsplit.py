import re

pattern = ' +'

temp = []
for line in open(r'listing.dat'):
    temp.append(int(re.split(pattern, line)[4]))

print(temp)
print()
print(sum(temp))
print()
print(sum(temp) / len(temp))
print()
print(min(temp))
print(max(temp))
