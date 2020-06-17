import sqlite3
from montrealDataScraper.montrealDataScraper.add_function.listReader import list_reader
from montrealDataScraper.montrealDataScraper.add_function.errorRecorder import error_recorder
from montrealDataScraper.montrealDataScraper.add_function.sql_command import sql_cmd
from montrealDataScraper.montrealDataScraper.add_function.report_db_handler import report_handler

class db_handler:
    def __init__(self, _debug_message_switch=False):
        self.conn =sqlite3.connect('montrealConfirmedCasesHistory_v2.db')
        self.report = report_handler()
        # self.conn =sqlite3.connect('testingFile_v2.db')
        self.DEBUG_MESSAGE = _debug_message_switch

    def close(self):
        self.report.close()
        self.conn.close()

    # testing command
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

# fetch all data from db file of a given borough, including: auto generated id, Name of borough, confirmed cases on that day, date when data is recorded, time when data is recorded
    def fetch_borough_inf(self,_boroughname):
        curr = self.conn.cursor();
        command_obj = sql_cmd(_boroughname)
        curr.execute(command_obj.borough_inf())
        self.conn.commit()
        rows = curr.fetchall()
        if (self.DEBUG_MESSAGE == True):
            print("\nDEBUG: Information on borough " +_boroughname+" :")
            for row in rows:
                print(row)
        return rows

# fetch all CORRECT data from db file of a given borough, including: auto generated id, Name of borough, confirmed cases on that day, date when data is recorded, time when data is recorded
    def fetch_0error_borough_inf(self, _boroughname):
        curr = self.conn.cursor();
        command_obj = sql_cmd(_boroughname)
        curr.execute(command_obj.borough_inf_0error())
        self.conn.commit()
        rows = curr.fetchall()
        if (self.DEBUG_MESSAGE == True):
            print("\nDEBUG: Information on borough " +_boroughname+" with 100% correct data :")
            for row in rows:
                print(row)
        return rows

# fetch only the case data of a given borough region
    def fetch_borough_case(self, _boroughname):
        # self.conn.row_factory = lambda cursor, row: row[0]
        # return cumulative case & date
        curr = self.conn.cursor();
        command_obj = sql_cmd(_boroughname)
        curr.execute(command_obj.borough_case())
        self.conn.commit()
        rows = curr.fetchall()

        if (self.DEBUG_MESSAGE == True):
            print("\nDEBUG: Cases each day on borough " +_boroughname+" :")
            for row in rows:
                print(row)
        return rows

# organize case list to remove record error from database
    def organize_borough_case(self, _boroughname):
        # self.conn.row_factory = lambda cursor, row: row[0]
        #return 0 error, cumulative case & date
        curr = self.conn.cursor();
        command_obj = sql_cmd(_boroughname)
        curr.execute(command_obj.borough_inf_0error_case_only())
        self.conn.commit()
        rows = curr.fetchall()
        # add last day's cumulative cases to report database
        self.report.cumulative_N_date(_boroughname,rows[-1][0],rows[-1][1])

        if (self.DEBUG_MESSAGE == True):
            print("\nDEBUG: Cases each day on borough " +_boroughname+" with 100% correct data:")
            for row in rows:
                print(row)
        return rows

    def fetch_borough_daily_new_case(self,_boroughname):
        # self.conn.row_factory = lambda cursor, row: row[0]
        #return 0 error, new cases & date
        curr = self.conn.cursor();
        command_obj = sql_cmd(_boroughname)
        curr.execute(command_obj.borough_daily_increase())
        self.conn.commit()
        rows = curr.fetchall()

        # add the day before last day's new case to report database
        self.report.new_case_N_date(_boroughname, rows[-1][0], rows[-1][1])

        if (self.DEBUG_MESSAGE == True):
            print("\nDEBUG: Daily case increase each day on borough " +_boroughname+" with 100% correct data:")
            for row in rows:
                print(row)
        return rows


# calculate the borough halftime of a given borough region in each day, return a list
    def fetch_borough_halftime_each_day(self, _boroughname):
        cases= self.fetch_borough_case(_boroughname)
        half_times = []
        for case in cases:
            half_num = int(case[0]/2)
            count = 0
            for _case in cases:

                if (half_num <= _case[0]):
                    break
                else:
                    count += 1

            if (count != 0 and case[0]>5):

                half_time = [case_data[0] for case_data in cases].index(case[0]) - count
            else:
                half_time = -1
            half_times.append([ case[0], half_time, case[1]]) #half time list will generate a list with 2 data in each line: case, and halftime

        if(self.DEBUG_MESSAGE==True):
            print("halftime of borough " + _boroughname + " in each day:")
            for line in half_times:
                print ("date: "+str(line[2])+" case: "+str(line[0])+", halftime: "+str(line[1]))

        return half_times

# from fetch_borough_halftime_each_day, remove the -1 data in list(unuseful data), return a list
    def fetch_organized_borough_halftime_list(self, _boroughname):
        # TODO: add date js
        double_time_list = self.fetch_borough_halftime_each_day(_boroughname)
        index = len(double_time_list)
        size = index
        for i in reversed(double_time_list):
            if (i[1] == -1):
                break
            index -= 1
        organized_double_time_list = []
        if (index == size):
            warning = error_recorder()
            warning.warning("Doubling time in "+_boroughname+" is greater than "+str(size)+" days, not enough data to plot a graph")
            return organized_double_time_list
        for i in range(index, size):
            organized_double_time_list.append([double_time_list[i][1],double_time_list[i][2]])
        return organized_double_time_list


#NOT USED
# calculate the average borough halftime of a given borough region. return an int
    def fetch_borough_average_halftime(self, _boroughname):
        halftime_list= self.fetch_borough_halftime_each_day(_boroughname)

        num_of_available_elements = 0
        sum = 0;
        for each_half_time in halftime_list:
            if (each_half_time[1] != -1):
                num_of_available_elements += 1
                sum += each_half_time[1]

            if (num_of_available_elements == 0):
                average_half_time = -1
            else:
                average_half_time = round(sum / num_of_available_elements, 2)

        if (self.DEBUG_MESSAGE == True):
            print("Average Halftime in", _boroughname, ":", average_half_time, "days")

        return average_half_time

# calculate all the average borough halftime in the list, return a list
    def fetch_all_average_halftime(self):
        borough_list = list_reader().get_list()
        halftime_list = []
        for boroughName in borough_list:
            # print("DEBUG: " + boroughName)
            half_time = self.fetch_borough_average_halftime(boroughName)
            halftime_list.append([boroughName, half_time])

        return halftime_list

#




#testing area


# test_dummy = db_handler(True)
# a_list = test_dummy.fetch_borough_case('Ahuntsic–Cartierville')
# a_list = test_dummy.fetch_borough_daily_new_case('Montréal-Est')
# a_list = test_dummy.organize_borough_case('Beaconsfield')

# a_list = test_dummy.fetch_borough_inf('Ahuntsic–Cartierville')
# a_list = test_dummy.fetch_0error_borough_inf('Montréal-Est')
# a_list = test_dummy.fetch_borough_halftime_each_day('Côte-Saint-Luc')
# b_list = test_dummy.fetch_organized_borough_halftime_list('Ahuntsic–Cartierville')



# #
# print ("\nTEST a: \n")
# for staff in a_list:
#     print(staff)
# print("\nTEST b: \n")
# for staff in b_list:
#     print(staff)

# print("next\n")

# test_dummy.fetch_0error_borough_inf('Ahuntsic–Cartierville')
# # halftime_list=test_dummy.fetch_all_average_halftime()
#
# cases = test_dummy.fetch_borough_halftime_each_day('Anjou')

# for halftime in halftime_list:
#     print(halftime)
# datas = test_dummy.fetch_borough_inf('Anjou')




