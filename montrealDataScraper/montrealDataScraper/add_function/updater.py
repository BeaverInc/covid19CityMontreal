from montrealDataScraper.montrealDataScraper.add_function.graphPlotter import graph_handler
from montrealDataScraper.montrealDataScraper.add_function.graphPlotter import list_reader
from datetime import datetime
import sqlite3
import os
#update element from database

class updater:
    def __init__(self, debug_switch = False):
        self.debug = debug_switch
        self.today = datetime.now().strftime("%A, %d %B %Y, %H:%M")


    def update_graph(self,update_graph = True):
        graph_updater = graph_handler(self.debug)
        graph_updater.draw_all(update_graph) # this will also update report database
        graph_updater.close()

    def update_borough_list(self):
        list_reader().update_js_list()

    def update_recorded_time_on_webside(self):
        self.web_path = os.path.abspath(__file__ + "/../../../")
        with open(os.path.join(self.web_path+"\\webpage\\js\\", 'recorded_time.js'), 'w', encoding='utf-8') as recorded_time:
            code = 'var record_time =" '+self.today+'."'
            recorded_time.write(code)

    def update_daily_report(self): #need to update graph first to update report database
        conn = sqlite3.connect('daily_report.db')
        curr = conn.cursor();
        curr.execute('''SELECT * FROM REPORT''')
        conn.commit()
        report = curr.fetchall()
        conn.close()
        web_path = os.path.abspath(__file__ + "/../../../")
        with open(os.path.join(web_path + "\\webpage\\js\\", 'current_data.js'), 'w', encoding='utf-8') as report_js:

            code = 'var '
            for line in report:
                # TODO: fix this
                name_in_js = str(line[1])
                for char in [' ',"'",'-','–']:
                    if char in name_in_js:
                        name_in_js = name_in_js.replace(char, "_")
                line_in_js = name_in_js+" = { cumulativeCases : "+str(line[2])+" , cumulativeCasesDate : '"+str(line[3])+"' , newCases : "+str(line[4])+" , newCasesDate : '"+str(line[5])+"' },\n"
                code += line_in_js
            code = code[: -2]
            code += " ;"
            report_js.write(code)

#
# dummy = updater()
# report = dummy.update_daily_report()

