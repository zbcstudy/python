import pymysql

db = pymysql.connect("localhost", "root", "123456", "test")

cursor = db.cursor()
data = cursor.execute("select version()")
print(cursor.fetchone())

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, CONT)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


db.close()
