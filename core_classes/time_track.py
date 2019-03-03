"Управління часом (додати, редагувати, видалити, запустити та зупинити таймер)."
import datetime as dt
import threading
from core_classes.basic_operations import TimeTracker
class Timer:
    task = []
    def __init__(self):
        pass

    def add_time(self, task):
        print(dt.datetime.now(task))
        user_choice = int(input("if you want to add time to start time choose 1\n"
                                "to add time to end time choose 2"))
        if user_choice == 1:
            self.task[task][0] += dt.timedelta(float(input("time in days")))
        elif user_choice == 2:
            self.task[task][1] += dt.timedelta(float(input("time in days")))

    def del_time(self, task):
        print(dt.datetime.now(task))
        user_choice = int(input("if you want to delete time in start time choose 1\n"
                                "and if you want to delete end time choose 2"))
        if user_choice == 1:
            self.task[task][0] = None
        elif user_choice == 2:
            self.task[task][1] = None

    def start_time(self, task):
        time_to_end = dt.datetime(task)
        time = threading.Timer(10.0)
        time.start()
        delta = (time_to_end - dt.datetime.today())
        if delta.total_seconds() <= 1:
            time.cancel()
        else:
            print(delta.seconds)
    def stop_timer(self, task):
        time = self.task[task[0]]
        time.cancel()

