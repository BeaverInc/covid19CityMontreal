from montrealDataScraper.montrealDataScraper.graphPlotter import graph_handler
import os
class updater:
    def __init__(self):
        graph_updater = graph_handler(False)
        graph_updater.draw_all()
