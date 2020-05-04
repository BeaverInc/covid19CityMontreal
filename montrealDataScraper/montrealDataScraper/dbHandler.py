import sqlite3

class db_handler:
    def __init__(self):
        self.conn = sqlite3.connect('testingFile_v2.db')
        # self.conn =sqlite3.connect('montrealConfirmedCasesHistory.db')
        self.curr = self.conn.cursor();

    def close(self):
        self.conn.close()

    def placeholder_exe(self):
        self.curr.execute(""" """)

        self.conn.commit()

    def printBorough(self,_boroughname):

        self.curr.execute("""
WITH Y AS
(with X as (SELECT
        id,
        boroughname,
        confirmedCase,
        Date,
        time
FROM
DATA
WHERE boroughname = '"""+_boroughname+"""')

SELECT *,
(SELECT Date FROM X X1
       WHERE X1.Date > X.Date
          OR X1.Date = X.Date AND X1.id > X.id
       ORDER BY Date , ID  LIMIT 1 ) next 
FROM
X
ORDER BY date, id)
select id, boroughname,confirmedcase,date,time
FROM
Y
WHERE
date <> next
AND
next <> 0
        """)
        self.conn.commit()
        print(self.curr.fetchall())

#testing
db_handler().printBorough('Ahuntsic–Cartierville')



