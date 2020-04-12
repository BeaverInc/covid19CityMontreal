import os, sys

class list_reader:
    def __init__(self):
        self.list = []
        with open(os.path.join(sys.path[0], "list.txt"), "r", encoding='utf-8') as borough_list:
            for line in borough_list:
                line = line.replace(u'\n',u'')
                line = line.replace(u'\ufeff', u'')
                self.list.append(line)

    def get_list(self):
        return self.list
