from montrealDataScraper.montrealDataScraper.add_function.updater import updater
from montrealDataScraper.montrealDataScraper.add_function.scrapy_runner import scrapy_updater

#For debug
# updater = updater(True)
# updater.update_graph(False)

scrapy_updater()
updater = updater()
updater.update_borough_list()
updater.update_graph()
updater.update_daily_report()
updater.update_recorded_time_on_webside()


