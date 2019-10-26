#!/usr/bin/python3
import sys

print(sys.argv)
user = pwd = host = None

port = 22 * 22  # default port
try:
    user = sys.argv[1]
    pwd = sys.argv[2]
    host = sys.argv[3]
    port = sys.argv[4]
except:
    pass

print('username :', user)
print('pwd :', pwd)
print('host :', host)
print('port :', port)
