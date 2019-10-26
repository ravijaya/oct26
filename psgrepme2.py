import re


pattern = '^r'
pattern2 = 'bash$'

log_file = 'passwd.txt'

for line in open(log_file):
    if re.search(pattern, line, re.I) and re.search(pattern2, line, re.I):
        print(line, end='')