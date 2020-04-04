import sqlite3

conn =sqlite3.connect('montrealConfirmedCasesHistory.db')
curr =conn.cursor();

curr.execute("""create table DATA(boroughName text, confirmedCase int, time TIME)""")

conn.commit()
conn.close()

