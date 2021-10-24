import sqlalchemy as sa
dbc = 'mysql+pymysql://root:@localhost:3306'
con = sa.create_engine(dbc)
con.execute('CREATE DATABASE school')
con.execute('USE  school')
sql = """CREATE  TABLE  stu (
    stuid   INTEGER       PRIMARY KEY,
    name   VARCHAR(50)  not null,
    pid     VARCHAR(20)  not null,
    phone   VARCHAR(20)  not null )"""
con.execute(sql)
sql="INSERT INTO stu VALUES (104001,'Claire','B342222','1245667')"
con.execute(sql)
result=con.execute("SELECT * FROM stu")
rows = result.fetchall()
print(rows)
con.execute('DROP  TABLE  stu')
con.execute('DROP  DATABASE  school')