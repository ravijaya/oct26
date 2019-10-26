import pyodbc

author = 'jaya'
version = '0.0.1'


def insert_row(conn, cursor, data):
    query = 'insert into passwd values(?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(query, data)
    conn.commit()


def db_connection(connection_string):
    """establish the connection"""
    conn = cursor = None

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
    except (pyodbc.ProgrammingError, pyodbc.Error) as err:
        print(err)

    return conn, cursor


def db_close(conn, cursor):
    """closing the connection"""
    cursor.close()
    conn.close()


if __name__ == '__main__':
    conn_str = 'Driver=SQLITE3;Database=oct24.sqlite;'
    print(db_connection(conn_str))
