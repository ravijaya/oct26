info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

item = 'version'

if item in info:  # validate for the key
    info[item] = 3.6   # update

info['arch'] = 'x86_64'  # adding item into the dict
print(info)
print(len(info))

