import sqlite3

conn = sqlite3.connect('db.sqlite3')
curs = conn.cursor()

query = 'SELECT * FROM mango'

curs.execute(query)

da = curs.fetchall()

print(da)