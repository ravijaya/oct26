from flask import Flask, render_template, request, redirect
from psmodel import db_close, db_connection, insert_row

conn_str = 'Driver=SQLITE3;Database=../oct24.sqlite;'
app = Flask(__name__)


@app.route('/addaction', methods=['POST'])
def add_user_action():
    conn, cursor = db_connection(conn_str)
    insert_row(conn, cursor, list(request.form.values()))
    db_close(conn, cursor)
    return redirect('/')   # url redirection


@app.route('/add')
def add_user():
    return render_template('addrecords.html')


@app.route('/')
def index():
    conn, cursor = db_connection(conn_str)
    query = 'select * from passwd'
    cursor.execute(query)

    headers = [col_info[0] for col_info in cursor.description]
    response = render_template('index.html', headers=headers, rows=cursor)
    db_close(conn, cursor)
    return response


if __name__ == '__main__':
    app.run(debug=True, )
