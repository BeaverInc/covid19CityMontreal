import os, sys
import json

class list_reader:
    def __init__(self):
        self.list_path = os.path.abspath(__file__ + "/../../")
        self.web_path = os.path.abspath(__file__ + "/../../../")
        self.list = []
        with open(os.path.join(self.list_path, "list.txt"), "r", encoding='utf-8') as borough_list:
            for line in borough_list:
                line = line.replace(u'\n',u'')
                line = line.replace(u'\ufeff', u'')
                self.list.append(line)

    def get_list(self):
        return self.list

    def to_json(self):
        name = {'name': self.list}

        with open(os.path.join(self.web_path+"\\webpage\\js\\", 'list.json'), 'w', encoding='utf-8') as outfile:

            json_file = json.dump(name, outfile, ensure_ascii=False)
