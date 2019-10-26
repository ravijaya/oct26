import pyodbc

# conn = pyodbc.connect('Driver={SQL Server};'
#                             'Server=CL******;'
#                             'Database=prod-**-db;'
#                             'Trusted_Connection=yes;')
try:
    conn = pyodbc.connect('Driver=SQLITE3;Database=oct24.sqlite;')
    cursor = conn.cursor()

    query = """
    create table passwd(
    login varchar(32),
    pwd varchar(4),
    uid int,
    gid int,
    gecos varchar(64),
    home varchar(32),
    shell varchar(32)
    )
    """
    cursor.execute(query)  # execute the query
    conn.commit()
    cursor.close()
    conn.close()
except pyodbc.Error as err:
    print(err)
except pyodbc.ProgrammingError as err:
    print(err)