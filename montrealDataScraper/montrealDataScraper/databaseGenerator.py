import sqlite3

# conn =sqlite3.connect('testingFile_v2.db')
conn =sqlite3.connect('montrealConfirmedCasesHistory_v2.db')
curr =conn.cursor();

curr.execute("""
create table DATA(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	boroughName text, 
	confirmedCase int, 
	date TIME, 
    time TIME)
""")

conn.commit()
conn.close()

