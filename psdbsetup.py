import json
"""http://collabedit.com/tfnjw"""

parameter = dict(Driver='{SQL Server};',
                 Server='CL******;',
                 Database='prod-**-db;',
                 Trusted_Connection='yes')

json.dump(parameter, open('dbconnect.json', 'w'))

print(json.dumps(parameter))