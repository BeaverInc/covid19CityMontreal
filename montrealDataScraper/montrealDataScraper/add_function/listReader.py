import os

class list_reader:
    def __init__(self):
        self.web_path = os.path.abspath(__file__ + "/../../../")
        self.list = []
        with open("list.txt", "r", encoding='utf-8') as borough_list:
            for line in borough_list:
                line = line.replace(u'\n',u'')
                line = line.replace(u'\ufeff', u'')
                self.list.append(line)

    def get_list(self):
        return self.list

    def update_js_list(self):
        with open(os.path.join(self.web_path+"\\webpage\\js\\", 'list.js'), 'w', encoding='utf-8') as js_list:
            code = 'var borough = ['

            for borough in self.list:
                line = '"'+borough+'", '
                code += line
            code = code[: -2]
            code += ']'

            js_list.write(code)


