"""csv 2 db"""

import csv
import pyodbc

content = [row for row in csv.reader(open('passwd.txt'), delimiter=':')]  # list comprehension

try:
    conn = pyodbc.connect('Driver=SQLITE3;Database=oct24.sqlite;')
    cursor = conn.cursor()

    query = """insert into passwd values (?, ?, ?, ?, ?, ?, ?)"""
    cursor.executemany(query, content)
    conn.commit()
    cursor.close()
    conn.close()
except pyodbc.Error as err:
    print(err)
except pyodbc.ProgrammingError as err:
    print(err)

