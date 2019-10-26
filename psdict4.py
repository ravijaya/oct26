info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': ['apache httpd',],
    'version': [2.2, 1, 2, 3, 4]
}

info['application'] = info.pop('app')
print(info)
