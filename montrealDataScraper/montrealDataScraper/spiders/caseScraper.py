import scrapy
from ..items import Borough
from .listReader import list_reader

import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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
            borough = boroughCol.xpath('td/text()').extract()
            # print(borough)

            _borough['boroughName'] = boroughName
            try:
                borough[1]= borough[1].replace(' ','')
                borough[1]= borough[1].replace('<', '')
                # print(borough[1])
                caseNum = int(borough[1])

            except ValueError:
                try:
                    # print(boroughCol.extract())
                    borough_expect = boroughCol.css('.bodytext').xpath('./text()').get()
                    caseNum = int(borough_expect)
                except:
                    caseNum = -1

            _borough['confirmedCase'] = caseNum

            _borough['time'] = now
            # print("end of borough")
            yield _borough





