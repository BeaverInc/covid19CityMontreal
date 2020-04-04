import scrapy
from ..items import Borough
import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class confirmedCaseSpider(scrapy.Spider):

    name = 'confirmedCases'
    start_urls = [
        'https://santemontreal.qc.ca/en/public/coronavirus-covid-19/'
    ]

    def parse(self, response):
        _borough = Borough()

        cityDataTable = response.xpath('//*[@id="c36473"]/div/table[2]/tbody')
        cityDatas = cityDataTable.css('tr')
        for cityData in cityDatas:
            borough = cityData.xpath('td/text()').extract()
            for id, boroughData in enumerate(borough):
                borough[id]=boroughData.replace(u'\xa0', u'')
            # print(borough)
            if len(borough) > 0:
                if(len(borough[0])>1):
                    _borough['boroughName'] = borough[0]
                    _borough['confirmedCase'] = (borough[1].replace('<',''))
                    _borough['time'] = now
            yield _borough



