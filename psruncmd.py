"""demo 4 the bytes"""
import sys
import subprocess
import re


class UnSupportedOSError(Exception):
    pass


if sys.platform == 'linux':
    cmd = ['ifconfig']
elif sys.platform == 'win32':
    cmd = ['ipconfig']
else:
    raise UnSupportedOSError('unsupported operating system')

# (.0-254){3}  .c.d
# a 1-254
op = subprocess.check_output(cmd)
pattern = '([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])'  #a
pattern += '(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])){3}'  # .b.c.d
pattern = fr'\b({pattern})\b'

print(pattern)
print()
for m in re.finditer(pattern, op.decode()):
    print(m.group())
#print(pattern)