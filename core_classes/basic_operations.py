import datetime as dt

"""Запуск через debug або інтерпертатор.
			Управління тайм трекерами (додати, редагувати, видалити).
			Управління задачами (додати, редагувати, видалити).
			


"""


class TimeTracker:
    task = []

    def __init_(self):
        self.task = []
    def add_task(self, task):
        print("enter start time in format year, month, day")
        sY = int(input("year?: "))
        sM = int(input("month?: "))
        sD = int(input("day? :"))
        start_date = dt.date(sY, sM, sD)
        print("enter end time in format year, month, day")
        eY = int(input("year?: "))
        eM = int(input("month?: "))
        eD = int(input("day? :"))
        end_date = dt.date(eY, eM, eD)
        self.task.append({task: (start_date.strftime("%Y/%m/%d"), end_date.strftime("%Y/%m/%d"))})
        return self.task

    def change_task(self, task):
        print("to change task choose 1\n"
              "to change start time choose 2\n"
              "to change end time choose 3")
        user_choice = int(input(""))
        if user_choice == "1":
            self.task[task] = input("new task name")
        elif user_choice == "2":
            self.task[task][0] = input("new start date")
        elif user_choice == "3":
            self.task[task][1] = input("new end date")

    def del_task(self, task):
        print("your task will be deleted\n"
              "do you want to continue?")
        user_choice = input("Y/N").lower()
        if user_choice == "y":
            del self.task[task]
        else:
            exit("your task is in place\n"
                 "thank you for saving life!")

