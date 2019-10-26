from os.path import getsize, getmtime
from time import ctime
from datetime import datetime

print(getsize('passwd.txt'))
print()
print(ctime(getmtime('passwd.txt')))
print()
print('current ts :', datetime.now())
