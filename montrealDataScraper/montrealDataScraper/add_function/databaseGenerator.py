import sqlite3
from montrealDataScraper.montrealDataScraper.add_function.listReader import list_reader

class database_generator:
    def __init__(self, _name):
        self.conn = sqlite3.connect(_name)
        self.curr = self.conn.cursor();

    def generate_covid_database(self):
        self.curr.execute("""
        create table DATA(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        	boroughName text, 
        	confirmedCase int, 
        	date TIME, 
            time TIME)
        """)
        self.conn.commit()
        self.conn.close()

    def generate_daily_report_database(self):
        self.curr.execute("""
        create table REPORT(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        	boroughName TEXT, 
        	cumulativeCases INT, 
        	cumulativeCasesDate TIME, 
        	newCases TEXT,
            newCasesDate TIME);
        """)

        borough_list = list_reader().get_list()
        for borough in borough_list:
            self.curr.execute('''
            INSERT INTO REPORT (boroughName,cumulativeCases ,cumulativeCasesDate,newCases,newCasesDate)
            VALUES ("'''+borough+'''",0 ,"0001-01-02",0,"0001-01-01");
            
            ''')

        self.conn.commit()
        self.conn.close()


# database_generator('montrealConfirmedCasesHistory_v2.db').generate_covid_database()

# database_generator('testingFile_v2.db').generate_covid_database()

database_generator('daily_report.db').generate_daily_report_database()



