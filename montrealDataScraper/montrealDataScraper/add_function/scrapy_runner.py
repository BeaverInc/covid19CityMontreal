from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class scrapy_updater:
    def __init__(self, _debug_message_switch=False):
        self.DEBUG_SWITCH = _debug_message_switch
        process = CrawlerProcess(get_project_settings())
        process.crawl('confirmedCases')
        process.start()
        if (self.DEBUG_SWITCH == True):
            print ("Scraping Information from Santé Montréal\n")

