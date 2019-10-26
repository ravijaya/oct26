"""random file processing"""

fp = open('passwd.txt', 'rb')   # read-binary

print(fp.tell())
print(fp.read(10))
print(fp.tell())

fp.seek(40, 1)
print(fp.tell())
print(fp.read(10))

fp.seek(-10, 2)
print(fp.tell())
print(fp.read(10))

fp.seek(0, 0)  #
print(fp.tell())
fp.close()