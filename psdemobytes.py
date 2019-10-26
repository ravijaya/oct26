"""demo for the bytes string"""

s = 'python'
print(s)
print(type(s))
print(s.encode())   # str into bytes
print()

s = b'python'
print(s)
print(type(s))
print(s.decode())  # bytes into str
