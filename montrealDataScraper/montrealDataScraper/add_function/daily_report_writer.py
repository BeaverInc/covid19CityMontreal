import sqlite3
from montrealDataScraper.montrealDataScraper.add_function.sql_command import sql_cmd

class reporter:
    def __init__(self, _debug_message_switch=False):
        self.conn = sqlite3.connect('daily_report.db')
        self.DEBUG_MESSAGE = _debug_message_switch

    def close(self):
        self.conn.close()

    def TESTING_COMMAND(self, _boroughname):
        curr = self.conn.cursor();
        command_obj = sql_cmd(_boroughname)
        curr.execute(command_obj.testing_command())
        self.conn.commit()
        rows = curr.fetchall()
        if (self.DEBUG_MESSAGE == True):
            print("\nDEBUG: TESTING COMMAND ON " + _boroughname + " :")
            for row in rows:
                print(row)
        return rows

