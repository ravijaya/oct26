info = {
    'host': 2.2,
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': [2.2, 3.4, 2.3, 1.2]
}

# iterate a dict for its key, value pair

print(info)
print()

keys = []

for key, value in info.items():
    if type(value) is list:
        if 2.2 in value:
            keys.append(key)

print(keys)
