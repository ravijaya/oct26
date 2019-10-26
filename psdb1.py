import pyodbc

# conn = pyodbc.connect('Driver={SQL Server};'
#                             'Server=CL******;'
#                             'Database=prod-**-db;'
#                             'Trusted_Connection=yes;')

conn = pyodbc.connect('Driver={SQLITE3}; Database=prod-**-db;')
cursor = conn.cursor()
query = 'select sqlite_version()'
cursor.execute(query)   # execute the query

print(cursor.rowcount)
# result = cursor.fetchone() # fetch the data from the resultset
# print(result)

cursor.close()
conn.close()
