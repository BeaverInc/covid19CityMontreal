from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from montrealDataScraper.montrealDataScraper.updater import updater

process = CrawlerProcess(get_project_settings())

process.crawl('confirmedCases')
process.start()

# #For debug
# updater = updater(True)

updater = updater()
updater.update_graph()
updater.update_borough_list()
updater.update_recorded_time_on_webside()


