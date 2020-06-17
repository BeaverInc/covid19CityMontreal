import matplotlib.pyplot as plt
from montrealDataScraper.montrealDataScraper.add_function.dbHandler import db_handler
from montrealDataScraper.montrealDataScraper.add_function.listReader import list_reader
import os



class graph_handler:
    def __init__(self, _debug_message_switch=False):
        self.database_handler = db_handler(_debug_message_switch)
        self.DEBUG_SWITCH = _debug_message_switch
        self.graph_folder_path = os.path.abspath(__file__ + "/../../../")

    def close(self):
        self.database_handler.close()

    def draw_testing(self, _boroughname):

        case_list = self.database_handler.organize_borough_case(_boroughname)
        size = len(case_list)
        days = []

        datas =[]
        for row in case_list:
            datas.append(row[0])
            days.append(row[1])
        plt.figure(figsize=(5.5, 4.4))
        fig, ax = plt.subplots()
        plt.grid(True)
        ax.xaxis.set_major_locator(plt.MaxNLocator(10))
        plt.plot(days, datas)
        fig.autofmt_xdate()

        plt.xlabel('Date')
        plt.ylabel('Cases')
        plt.title("Confirmed cases in "+_boroughname)
        file_name = _boroughname+'_c.png'
        plt.savefig(os.path.join(self.graph_folder_path +"\\webpage\\graph\\", file_name))
        plt.clf()

    def draw_borough_daily_case(self, _boroughname, update = True):
        case_list = self.database_handler.organize_borough_case(_boroughname)
        if (update == True):
            size = len(case_list)
            days = []

            datas = []
            for row in case_list:
                datas.append(row[0])
                days.append(row[1])
            plt.figure(figsize=(5.5, 4.4))
            fig, ax = plt.subplots()
            plt.grid(True)
            ax.xaxis.set_major_locator(plt.MaxNLocator(10))
            plt.plot(days, datas)
            fig.autofmt_xdate()

            plt.xlabel('In Last ' + str(size) + ' Days')
            plt.ylabel('Cases')
            plt.title("Confirmed cases in " + _boroughname)
            file_name = _boroughname + '_c.png'
            plt.savefig(os.path.join(self.graph_folder_path + "\\webpage\\graph\\cases\\", file_name))
            plt.clf()


    def draw_borough_daily_double_time(self, _boroughname, update = True):
        double_time_list = self.database_handler.fetch_organized_borough_halftime_list(_boroughname)
        if (update == True):
            size = len(double_time_list)
            days = []

            datas = []
            for row in double_time_list:
                datas.append(row[0])
                days.append(row[1])
            plt.figure(figsize=(5.5, 4.4))
            fig, ax = plt.subplots()
            plt.gca().invert_yaxis()
            plt.grid(True)
            ax.xaxis.set_major_locator(plt.MaxNLocator(10))
            plt.plot(days, datas)
            fig.autofmt_xdate()

            plt.xlabel('In Last ' + str(size) + ' Days')
            plt.ylabel('Doubling Time (Days)')
            plt.title("Doubling Time in  " + _boroughname)
            file_name = _boroughname + '_d.png'
            plt.savefig(os.path.join(self.graph_folder_path + "\\webpage\\graph\\double_time\\", file_name))
            plt.clf()


    def draw_borough_daily_new_case(self, _boroughname, update = True):
        case_list = self.database_handler.fetch_borough_daily_new_case(_boroughname)

        if (update== True):
            size = len(case_list)
            days = []

            datas = []
            for row in case_list:
                datas.append(row[0])
                days.append(row[1])
            plt.figure(figsize=(5.5, 4.4))
            fig, ax = plt.subplots()
            plt.grid(True)
            ax.xaxis.set_major_locator(plt.MaxNLocator(10))
            plt.plot(days, datas)
            fig.autofmt_xdate()

            plt.xlabel('In Last ' + str(size) + ' Days')
            plt.ylabel('Cases')
            plt.title("New cases in " + _boroughname + " everyday")

            file_name = _boroughname + '_n.png'
            plt.savefig(os.path.join(self.graph_folder_path + "\\webpage\\graph\\new\\", file_name))
            plt.clf()


    def draw_all(self, update = True):
        update_graph = update
        borough_list = list_reader().get_list()
        for boroughName in borough_list:
            self.draw_borough_daily_case(boroughName, update_graph)
            self.draw_borough_daily_double_time(boroughName, update_graph)
            self.draw_borough_daily_new_case(boroughName, update_graph)

#testing area

# test_dummy = graph_handler(False)
# test_dummy.draw_testing("Ahuntsic–Cartierville")
# test_dummy.draw_borough_daily_case("Ahuntsic–Cartierville")
# test_dummy.draw_borough_daily_new_case("Ahuntsic–Cartierville")
# test_dummy.draw_borough_daily_double_time("Ahuntsic–Cartierville")
# test_dummy.draw_all()





