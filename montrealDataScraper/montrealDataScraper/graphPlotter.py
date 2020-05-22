import matplotlib.pyplot as plt
from montrealDataScraper.montrealDataScraper.dbHandler import db_handler
from montrealDataScraper.montrealDataScraper.spiders.listReader import list_reader


class graph_handler:
    def __init__(self, _debug_message_switch=False):
        self.database_handler = db_handler(_debug_message_switch)
        self.DEBUG_SWITCH = _debug_message_switch



    def draw_borough_daily_case(self, _boroughname):
        case_list = self.database_handler.organize_borough_case(_boroughname)
        size = len(case_list)
        days = []
        for i in range(1, size+1):
            days.append(i)

        plt.plot(days, case_list)
        plt.xlabel('Days')
        plt.ylabel('Cases')
        plt.title("Confirmed cases in "+_boroughname)
        plt.savefig("graph/cases/"+_boroughname+'_c.png')
        plt.clf()

    def draw_borough_daily_double_time(self, _boroughname):
        double_time_list = self.database_handler.fetch_organized_borough_halftime_list(_boroughname)
        size = len(double_time_list)
        days = []
        for i in range(1, size+1):
            days.append(i)
        plt.plot(days, double_time_list)
        plt.xlabel('Last '+str(size)+' Days')
        plt.ylabel('Doubling Time (Days)')
        plt.title("Doubling Time in  "+_boroughname)
        plt.savefig("graph/double time/"+_boroughname+'_d.png')
        plt.clf()

    def draw_all(self):
        borough_list = list_reader().get_list()
        for boroughName in borough_list:
            self.draw_borough_daily_case(boroughName)
            self.draw_borough_daily_double_time(boroughName)

#testing area

# test_dummy = graph_handler(False)
# test_dummy.draw_all()





