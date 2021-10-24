import sqlite3
con=sqlite3.connect('school.db')
cur=con.cursor()
cur.execute('DROP TABLE stu')
cur.execute('''CREATE TABLE stu
(   stuid   INTEGER       PRIMARY KEY,
    name   VARCHAR(50)   not null,
    pid     VARCHAR(20)   not null,
    phone   VARCHAR(20)   not null)''' )
cur.execute("INSERT INTO stu VALUES (104001,'Claire','B342222','1245667')")
cur.execute('SELECT * FROM stu')
rows=cur.fetchall()
print(rows)
cur.close()