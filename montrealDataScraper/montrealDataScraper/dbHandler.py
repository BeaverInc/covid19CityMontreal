import sqlite3
from montrealDataScraper.montrealDataScraper.spiders.listReader import list_reader
from montrealDataScraper.montrealDataScraper.errorRecorder import error_recorder

class db_handler:
    def __init__(self, _debug_message_switch=False):
        # # this is used for debug
        # self.conn = sqlite3.connect('testingFile_v2.db')
        self.conn =sqlite3.connect('montrealConfirmedCasesHistory_v2.db')
        self.curr = self.conn.cursor();
        self.DEBUG_MESSAGE = _debug_message_switch

    def close(self):
        self.conn.close()

    def placeholder_exe(self):
        self.curr.execute(""" """)

        self.conn.commit()

# fetch all data from db file of a given borough, including: auto generated id, Name of borough, confirmed cases on that day, date when data is recorded, time when data is recorded
    def fetch_borough_inf(self,_boroughname):
        data_list =[]
        if (self.DEBUG_MESSAGE == True):
            print("\nDEBUG: " + _boroughname)
        self.curr.execute('''
WITH Y AS
(with X as (SELECT
        id,
        boroughname,
        confirmedCase,
        Date,
        time
FROM
DATA
WHERE boroughname = "'''+_boroughname+'''")

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
        ''')
        self.conn.commit()
        rows = self.curr.fetchall()
        if (self.DEBUG_MESSAGE == True):
            print("Information of borough "+_boroughname+" :")
            for row in rows:
                data_list.append(row)
                print(row)
        else:
            for row in rows:
                data_list.append(row)
        return data_list

# fetch only the case data of a given borough region
    def fetch_borough_case(self, _boroughname):
        cases=[]
        datas = self.fetch_borough_inf(_boroughname)
        for data in datas:
            cases.append(data[2])
        return cases

# organize case list to remove record error from database
    def organize_borough_case(self, _boroughname):
        case_list = self.fetch_borough_case(_boroughname)

        index = len(case_list)
        size = index
        for i in reversed(case_list):
            if (i == -1):
                break
            index -= 1
        organized_case_list = []
        if (index == size):
            print("Not enough record to create list")
            return organized_case_list
        for i in range(index, size):
            organized_case_list.append(case_list[i])
        return organized_case_list
        return cases

# calculate the borough halftime of a given borough region in each day, return a list
    def fetch_borough_halftime_each_day(self, _boroughname):
        cases= self.fetch_borough_case(_boroughname)
        half_times = []
        for case in cases:
            half_num = int(case/2)
            count = 0
            for _case in cases:

                if (half_num <= _case):
                    break
                else:
                    count += 1

            if (count != 0 and case>5):
                half_time = cases.index(case) - count
            else:
                half_time = -1
            half_times.append([ case, half_time]) #half time list will generate a list with 2 data in each line: case, and halftime

        if(self.DEBUG_MESSAGE==True):
            print("halftime of borough " + _boroughname + " in each day:")
            for line in half_times:
                print ("day: "+str(half_times.index(line))+" case: "+str(line[0])+", halftime: "+str(line[1]))

        return half_times

# from fetch_borough_halftime_each_day, remove the -1 data in list(unuseful data), return a list
    def fetch_organized_borough_halftime_list(self, _boroughname):
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
            organized_double_time_list.append(double_time_list[i][1])
        return organized_double_time_list

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
# # halftime_list=test_dummy.fetch_all_average_halftime()
#
# cases = test_dummy.fetch_borough_halftime_each_day('Anjou')

# for halftime in halftime_list:
#     print(halftime)
# datas = test_dummy.fetch_borough_inf('Anjou')




