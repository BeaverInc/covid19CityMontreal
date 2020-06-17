import os, sys
from datetime import datetime

class error_recorder:
    def __init__(self):
        self.today = str(datetime.now())

    def warning(self, _message, auto_close = True):
        self.new_error_message = open("warningLog.txt", "a", encoding='utf-8')
        self.write(_message)

    def error(self, _message, auto_close = True):
        self.new_error_message = open("errorLog.txt", "a", encoding='utf-8')
        self.write(_message)

    def write(self, _message, auto_close = True):
        self.new_error_message.write(_message+" occurs on "+ self.today +"\n")
        if (auto_close == True):
            self.close_error_recorder()

    def close_error_recorder(self):
        self.new_error_message.close()

# test_dummy = error_recorder()
# test_dummy.write("2 errors occurs")




