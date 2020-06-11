from montrealDataScraper.montrealDataScraper.graphPlotter import graph_handler
from montrealDataScraper.montrealDataScraper.graphPlotter import list_reader
from datetime import datetime
import os
#update element from database

class updater:
    def __init__(self, debug_switch = False):
        self.debug = debug_switch
        self.today = datetime.now().strftime("%A, %d %B %Y, %H:%M")


    def update_graph(self):
        graph_updater = graph_handler(self.debug)
        graph_updater.draw_all()

    def update_borough_list(self):
        list_reader().update_js_list()

    def update_recorded_time_on_webside(self):
        self.web_path = os.path.abspath(__file__ + "/../../")
        with open(os.path.join(self.web_path+"\\webpage\\js\\", 'recorded_time.js'), 'w', encoding='utf-8') as recorded_time:
            code = 'var record_time =" '+self.today+'."'
            recorded_time.write(code)


