import re


pattern = '^r'
pattern = 'bash$'
pattern = '^$'
pattern = 'b.t'
pattern = 'b[aeiou]t'
pattern = 'b[^aeiou]t'
pattern = r'\b[6-9][0-9]{9}\b'
pattern = '\$2\.15'
pattern = '^root|^ravi'  # alternative
'[1-9][0-9]*'
pattern = r'\b([5-9][0-9][0-9])\b|\b([1-9][0-9]{3}[0-9]*)\b'
pattern = r'\b([5-9][0-9][0-9])\b|\b([1-9][0-9][0-9][0-9]+)\b'
pattern = r'\b([5-9]\d\d)\b|\b([1-9]\d\d\d+)\b'
pattern = r'\b([5-9]\d{2})\b|\b([1-9]\d{3,})\b'

# pattern = r'\b(([5-9][0-9][0-9])|([1-9][0-9][0-9][0-9]+))\b'

log_file = 'passwd.txt'

for line in open(log_file):
    if re.search(pattern, line, re.I):
        print(line, end='')