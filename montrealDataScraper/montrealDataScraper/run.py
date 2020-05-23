from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from montrealDataScraper.montrealDataScraper.updater import updater

process = CrawlerProcess(get_project_settings())

process.crawl('confirmedCases')
process.start()

updater()
