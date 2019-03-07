# import datetime as dt
import time
from core_classes.task import *


class Time:
    def __init__(self):
        pass

    def add_time(self):
        """adding time in our task"""
        add_time = float(input("time to add: "))
        return dt.timedelta(add_time)

    def change_time(self, time):
        """changing time in task"""
        time = dt.datetime.now()
        return time

    def del_time(self, time):
        """deleting time"""
        del time

    def start_time(self):
        """starting point of execution"""
        t = time.time()
        return t

    def stop_time(self):
        """ending point of execution"""
        t = time.time()
        return t
