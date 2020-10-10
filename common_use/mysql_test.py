import mysql.connector
import datetime, time

DB_USER = 'root'
DB_PASS = 'sneakerhead'
DB_HOST = '10.0.0.131'
DB = 'vo_account'


def connect():
    cnx = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB)
    cursor = cnx.cursor()
    query = "SELECT * from mt_text"
    cursor.execute(query)
    rows = []
    for arr in cursor:
        print(arr)
        rows.append(arr)
    print(rows)


if __name__ == '__main__':
    connect()
    print(time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
    print(time.ctime())
    print(time.asctime(time.localtime()))
