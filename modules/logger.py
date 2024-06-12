import os
import datetime
import time
from time import perf_counter


class Logger():
    """
    A Class to log infomation to a txt file

    ...

    Attributes
    __________
    path : str
        the full path to the log-file e.g. 'c:/folder/to/where/the/file/is/located/log.log'
        if no path is set it uses the path to the python file running this class and creates a 'log.log' file
    debug : bool
        if set to True, criticals and warnings won't be counted
        default is False

    Methods
    _________
    start()
        starting the logger

    end() 
        ends the logger

    info(msg)
        writes a INFO line to the log-file

    warning(msg)
        writes a WARNING line to the log-file

    critical(msg)
        writes a CRITICAL line to the log-file

    checklog(type) returns bool
        checks for criticals, warnings or both
        default is 'criticals'
        can be set to 'criticals', 'warnings' or 'both'

    """
    def __init__(self, path = None, debug = False):
        self.path = path
        self.start_time = perf_counter()
        self.__warnings = 0
        self.__criticals = 0
        self.debug = debug
        if self.path is None:
            self.path = os.path.join(os.getcwd(), 'log.log')

    def __get_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __write(self, msg):
        self.msg = msg
        with open(self.path, 'a', encoding='utf-8') as file:
            file.write(self.msg + '\n')

    def start(self):
        self.msg = f"{self.__get_time()} : INFO     : Starting"
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(self.msg + '\n')

    def info(self, msg):
        self.msg = f"{self.__get_time()} : INFO     : {msg}"
        self.__write(self.msg)

    def critical(self, msg):
        self.msg = f"{self.__get_time()} : CRITICAL : {msg}"
        self.__write(self.msg)
        if self.debug == False:
            self.__criticals += 1

    def warning(self, msg):
        self.msg = f"{self.__get_time()} : WARNING  : {msg}"
        self.__write(self.msg)
        if self.debug == False:
            self.__warnings += 1

    def end(self):
        elapsed_time = perf_counter() - self.start_time
        elapsed = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))
        msgs = []
        msgs.append(f"{self.__get_time()} : INFO     : Ending")
        msgs.append(f"{self.__get_time()} : INFO     : Time used : {elapsed}")
        if self.__warnings == 1: 
            warning_txt = 'Warning'
        else:
            warning_txt = 'Warnings'
        if self.__criticals == 1:
            critical_txt = 'Critical'
        else:
            critical_txt = 'Criticals'
        msgs.append(f"{self.__get_time()} : INFO     : Ended with {self.__warnings} {warning_txt} and {self.__criticals} {critical_txt}")
        for msg in msgs:
            self.__write(msg)

    def checklog(self, type='both') -> bool:
        """Choose between 'criticals', 'warnings', 'both'
        Returns False if any type is flagged else True"""
        self.type = type.lower()
        if self.type not in ['criticals', 'warnings', 'both']:
            self.critical('Wrong check type')
            return False
        if self.type == 'criticals' and self.__criticals > 0:
            return False
        elif self.type == 'warnings' and self.__warnings > 0:
            return False
        elif self.type == 'both' and (self.__criticals > 0 or self.__warnings > 0):
            return False        
        else:
            return True      
