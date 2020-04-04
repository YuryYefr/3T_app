import datetime as dt

from core_classes.logic.sys_control import task_control, track_control
from core_classes.main_objects.tracker import Tracker
from core_classes.main_objects.files import *
from core_classes.main_objects.users import *
from core_classes.main_objects.timer import *
from core_classes.main_objects.task import Task
from core_classes.database.db_create import *
from core_classes.currency_exchange.currency_exchange.tester import *
dir_path = "C:/Users/123/PycharmProjects/3T_app/storage/"
user_help = None


def user_name():
    """our main logic"""
    user_name = UserName().user_create()
    print("checking for actual trackers")
    list_files()

    print(f"Welcome {user_name.user_name}!\n"
          "1.if you want to change trackers\n"
          "2.if you want to start new task \n"
          "3.if you want to start new tracker")
    user_choice = input("you choose?: ")
    while user_choice.isalpha():
        print("choose number")
        user_choice = input("you choose?: ")
    if user_choice == "1":
        if user_name.user_name != admin:
            raise Exception("you don't have permission")
        else:
            try:
                (task_control(track_control()))
            except Exception as e:
                print(e)
    elif user_choice == "2":
        try:
            user_tracker = input("tracker name? :")
            result = TasksIO(dir_path, user_tracker).read_file()

            if result.tracker_name == user_tracker:
                print(f'founded {user_tracker} tasks in storage\n'
                      f'do you want to proceed with your tracker?')
                user_choice = input("y/n: ").lower()
                if user_choice != 'y':
                    exit('shutting down the program')
                else:
                    user_tracker = result
                    user_task = Task().start_new_task(user_name)
                    start = Time().start_time()
                    user_task.some_code = input("some code")
                    stop = Time().stop_time()
                    user_task.end_date = dt.datetime.now()
                    user_task.duration = stop - start
                    user_tracker.task.append(user_task)

                    TasksIO(dir_path, user_tracker).write_file()
                    data_retrieve(user_tracker.tracker_name)
                    test_convert(*convert_args)
                    db()
                    exit("saving and shutting down")
            elif result != user_tracker:
                print('\t nothing yet created\n'
                      '\tcreating a new tracker :')
                user_task = Task().start_new_task(user_name)
                user_tracker = Tracker(user_task).start_track(user_name, user_task)
                user_tracker.task.append(user_task)
                data_retrieve(user_tracker.tracker_name)
                db()
                exit("shutting down the program")

        except Exception as e:
            print(e)
    else:
        user_define(user_name)


def user_define(user_name):
    """in case nothing created"""
    user_task = Task().start_new_task(user_name)
    new_tracker = Tracker([user_task]).start_track(user_name, [user_task])
    user_choice = input("do you want to start task?: y/n").lower()
    if user_choice != "y":
        exit("shutting down the program")

    print("you have created a new task")
    while user_choice not in "y/n":
        print("something wrong")
        user_choice = input("do you want to start task?: y/n").lower()
    print("1.start task\n"
          "2.change task name\n"
          "3.to delete task\n"
          "4.to look at your current progress")
    user_choice = input("you choose?: ")
    while user_choice.isalpha():
        print("choose from the list")
        user_choice = input("you choose?: ")
    if user_choice == "1":
        start = Time().start_time()
        user_task.user_code = input("some code")
        stop = Time().stop_time()
        user_task.end_date = dt.datetime.now()
        user_task.duration = stop - start
        TasksIO(dir_path, new_tracker).write_file()
        db()
        exit("saving and shutting down")

    elif user_choice == "2":
        user_new_task_name = input("and new name is?: ")
        user_task.change_task(user_new_task_name)
        print(user_task)
    elif user_choice == "3":
        Task().del_task()
        exit("you task is deleted")

    elif user_choice == "4":
        print(user_task)
        print("1.start task\n"
              "2.change task name\n"
              "3.to delete task\n"
              "4.to look at your current progress")
        user_choice = input("you choose?: ")
        while user_choice.isalpha():
            print("choose from the list")
            user_choice = input("you choose?: ")
        if user_choice == "1":
            start = Time().start_time()
            user_task.user_code = input("some code")
            stop = Time().stop_time()
            user_task.end_date = dt.datetime.now()
            user_task.duration = stop - start
            TasksIO(dir_path, user_task).write_file()

        elif user_choice == "2":
            user_new_task_name = input("and new name is?: ")
            user_task.change_task(user_new_task_name)
            print(user_task)
        elif user_choice == "3":
            Task().del_task()
            exit("you task is deleted")

user_name()