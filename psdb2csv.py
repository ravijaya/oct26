import csv
import pyexcel
import psmodel


def db_to_xlsx(xlsx_file):
    conn_str = 'Driver=SQLITE3;Database=oct24.sqlite;'
    connection, cursor = psmodel.db_connection(conn_str)

    query = 'select * from passwd';
    cursor.execute(query)
    headers = [col_info[0] for col_info in cursor.description]
    # print(headers)
    rows = [row for row in cursor]
    rows.insert(0, headers)
    pyexcel.save_as(dest_file_name=xlsx_file, array=rows)


def db2csv(csv_file):
    """function definition """
    conn_str = 'Driver=SQLITE3;Database=oct24.sqlite;'
    connection, cursor = psmodel.db_connection(conn_str)

    query = 'select * from passwd';
    cursor.execute(query)

    fw = csv.writer(open(csv_file, 'w', newline='\n'))
    rows = [(row[0], row[-1]) for row in cursor]
    fw.writerows(rows)

    psmodel.db_close(connection, cursor)


if __name__ == '__main__':
    # db2csv('passwd.csv')  # call
    db_to_xlsx('passwd.xlsx')
