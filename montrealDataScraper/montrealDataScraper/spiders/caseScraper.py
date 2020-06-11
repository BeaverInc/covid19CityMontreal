import scrapy
import winsound
from ..items import Borough
from .listReader import list_reader
from montrealDataScraper.montrealDataScraper.errorRecorder import error_recorder

import datetime
date_now = datetime.datetime.now().strftime("%Y-%m-%d")
time_now = datetime.datetime.now().strftime("%H:%M:%S")


class confirmedCaseSpider(scrapy.Spider):

    name = 'confirmedCases'
    start_urls = [
        # 'https://santemontreal.qc.ca/en/public/coronavirus-covid-19/'
        'https://santemontreal.qc.ca/en/public/coronavirus-covid-19/situation-of-the-coronavirus-covid-19-in-montreal/'
    ]

    def parse(self, response):
        # since Sante Montreal is constantly updating in this evolving situation, constant xpath is not reliable. A more human behaviour approach is used: from menus link -> title -> table where data is stored.
        _borough = Borough()
        borough_list = list_reader().get_list()
        error = error_recorder()

        # print(borough_list)
        # print('Debug:')

        for boroughName in borough_list:
            # print(boroughName)
            boroughCol = response.xpath("//tr[contains(., $val)]", val=boroughName)
            if not boroughCol:
                # print("error on ",boroughName )
                error.error("Did not find any information on " + str(boroughName))
                continue
            # print(boroughCol.extract())
            borough = boroughCol.xpath('td/text()').extract()

            # print(boroughName," : ",borough)
            _borough['boroughName'] = boroughName
            # print(borough)
            # print(borough[1])
            try:
                #some of the col in santemontrea has a dfferent css style so the name of the borough is missing from the line, in this situation the order of the reading need to be shifted by 1
                if(boroughName in borough[0]):
                    pNum = 1
                else:
                    pNum = 0

                borough[pNum] = borough[pNum].replace(' ', '')
                borough[pNum] = borough[pNum].replace('<', '')
                borough[pNum] = borough[pNum].replace(',', '')
                caseNum = int(borough[pNum])

            except ValueError:
                try:
                    # print(boroughCol.extract())
                    borough_expect = boroughCol.css('.bodytext').xpath('./text()').get()
                    caseNum = int(borough_expect)
                except:
                    caseNum = -1
                    winsound.Beep(440, 1000) # warn the user that an error has when scraping data

                    error.error("Unresolved Error fetched to database in borough "+str(boroughName))

            _borough['confirmedCase'] = caseNum
            # print(boroughName," : ",caseNum,"\ntime:", date_now , time_now,"\n")
            _borough['date'] = date_now
            _borough['time'] = time_now
            # print("end of borough")
            yield _borough


