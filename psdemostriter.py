"""demo for the python iterator"""

s = 'this is a sample string in python'
# print(s.index('sam'))

for temp in s[s.index('sam'):]:     # python's iterator
    print(temp, ':', ord(temp))


