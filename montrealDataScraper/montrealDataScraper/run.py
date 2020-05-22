from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from montrealDataScraper.montrealDataScraper.graphPlotter import graph_handler



process = CrawlerProcess(get_project_settings())

process.crawl('confirmedCases')
process.start()

graph_updater = graph_handler(False)
graph_updater.draw_all()