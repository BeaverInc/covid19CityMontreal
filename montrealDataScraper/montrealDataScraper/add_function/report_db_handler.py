import sqlite3
from montrealDataScraper.montrealDataScraper.add_function.sql_command import sql_cmd

class report_handler:
    def __init__(self, _debug_message_switch=False):
        self.conn =sqlite3.connect('daily_report.db')
        self.DEBUG_MESSAGE = _debug_message_switch

    def close(self):
        self.conn.close()

    # add last day's cumulative cases to report database
    def cumulative_N_date(self,_boroughname,cumulative,date):
        curr = self.conn.cursor();
        curr.execute(sql_cmd(_boroughname).update_cumulative_N_date(cumulative,date))
        self.conn.commit()
        curr.fetchall()

    # add last day's new case to report database
    def new_case_N_date(self,_boroughname,new_case,date):
        curr = self.conn.cursor();
        curr.execute(sql_cmd(_boroughname).update_new_case_N_date(new_case,date))
        self.conn.commit()
        curr.fetchall()