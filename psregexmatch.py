import re


s = 'the python and the perl scripting'
pattern = 'P.+?N'  # non-greedy match  .*, .+

m = re.search(pattern, s, re.I)

if m:
    print('match string :', m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print('failed to match')
