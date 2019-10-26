"""csv 2 db"""

import pyodbc

try:
    conn = pyodbc.connect('Driver=SQLITE3;Database=oct24.sqlite;')
    cursor = conn.cursor()
    print(cursor)
    query = """select * from passwd"""
    cursor.execute(query)
    print(cursor.fetchmany(2))
    # for row in cursor:
    #     print(row)
    #
    # cursor.close()
    conn.close()
except pyodbc.Error as err:
    print(err)
except pyodbc.ProgrammingError as err:
    print(err)
