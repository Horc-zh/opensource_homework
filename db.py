import os

db_file = "example.db"
if os.path.exists(db_file):
    os.remove(db_file)
import sqlite3

con = sqlite3.connect(db_file)
cursor = con.cursor()
cursor.execute(
    """CREATE TABLE stocks
          (date text, trans text, symbol text, qty real, price real)"""
)

cursor.execute(
    """INSERT INTO stocks VALUES 
          ('2006-01-05','BUY','RHAT',100,35.14)"""
)

cursor.execute(
    """INSERT INTO stocks VALUES 
          ('2006-02-05','BUY','FED',200,35.24)"""
)

for item in cursor.execute("select * from stocks"):  # 直接用循环遍历查询结果
    print(item)

t = ("RHAT",)
cursor.execute("SELECT * FROM stocks WHERE symbol=?", t)  # 使用内置的替换，减少安全风险
print(cursor.fetchone())

purchases = [
    ("2006-03-28", "BUY", "IBM", 1000, 45.00),
    ("2006-04-05", "BUY", "MSFT", 1000, 72.00),
    ("2006-04-06", "SELL", "IBM", 500, 53.00),
]
cursor.executemany("INSERT INTO stocks VALUES (?,?,?,?,?)", purchases)

sql = """create table news (id integer, score integer, title text, href text);
insert into news values (1, 8, "hello world", "http://oscar-lab.org");
insert into news values (2, 2, "hello charlie", "http://www.dlut.edu.cn");"""  # sql语句间要用分号分隔
cursor.executescript(sql)

print(list(cursor.execute("select * from news")))

con.row_factory = sqlite3.Row
c = con.cursor()
c.execute("select * from stocks")

r = c.fetchone()
print(type(r))

r.keys()

for field in r:
    print(field)

con.close()
