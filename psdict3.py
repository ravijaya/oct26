info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

del info['domain'], info['app']

print(info.pop('desc'))  # delete
print()
print(info)