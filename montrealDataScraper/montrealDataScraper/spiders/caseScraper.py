import scrapy
from ..items import Borough
from .listReader import list_reader

import datetime
date_now = datetime.datetime.now().strftime("%Y-%m-%d")
time_now = datetime.datetime.now().strftime("%H:%M:%S")


class confirmedCaseSpider(scrapy.Spider):

    name = 'confirmedCases'
    start_urls = [
        'https://santemontreal.qc.ca/en/public/coronavirus-covid-19/'
    ]

    def parse(self, response):
        # since Sante Montreal is constantly updating in this evolving situation, constant xpath is not reliable. A more human behaviour approach is used: from menus link -> title -> table where data is stored.
        _borough = Borough()
        borough_list = list_reader().get_list()

        # print(borough_list)
        # print('Debug:')

        for boroughName in borough_list:
            # print(boroughName)
            boroughCol = response.xpath("//tr[contains(., $val)]", val=boroughName)
            # print(boroughCol.extract())
            borough = boroughCol.xpath('td/text()').extract()
            # print(borough)

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
                    print("Unresolved Error fetched to database")

            _borough['confirmedCase'] = caseNum

            _borough['date'] = date_now
            _borough['time'] = time_now
            # print("end of borough")
            yield _borough





