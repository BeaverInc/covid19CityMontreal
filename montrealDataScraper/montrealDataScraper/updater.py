from montrealDataScraper.montrealDataScraper.graphPlotter import graph_handler
import os
class updater:
    def __init__(self, debug_switch = False):
        graph_updater = graph_handler(debug_switch)
        graph_updater.draw_all()
