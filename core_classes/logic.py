from core_classes.task_file_ops import *
from core_classes.timer import *
from core_classes.task import *
from core_classes.tracker import Tracker
from core_classes.files import *
admin = "yuriyefr".capitalize()
dir_path = "C:/Users/123/PycharmProjects/3T_app/storage/"
user_help = None


def user_name():
    user_name = input("what is your name?: ").capitalize()
    while user_name.isdigit():
        print("your name should be in letters")
        user_name = input("what is your name?: ").capitalize()
    print(f"Welcome {user_name}!\n"
          "1.if you want to change time track name\n"
          "2.if you want to delete your time track\n"
          "3.if you want to proceed with one of your time trackers\n")
    list_files()
    user_choice = input("you choose?: ")
    while user_choice.isalpha():
        print("choose number")
        user_choice = input("you choose?: ")
    if user_choice == "1":
        track_name = input("what tracker? :")
        new_track_name = input("new name is")
        Tracker(track_name).change_name(new_track_name)
    elif user_choice == "2":
        user_choice = input("tracker name?: ")
        Tracker(user_choice).del_track(user_choice)
    else:
        list_files()
    if user_name == admin:
        raise NotImplementedError
    user_tracker = input("tracker name? :")
    print("checking for actual trackers")
    try:
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
        elif result != user_tracker:
            print('\t nothing yet created\n'
                  '\tcreating a new tracker :')

    except Exception as e:
        print(e)
    user_define(user_name)


def user_define(user_name):
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
        new_tracker.task.append(user_task)
        TasksIO(dir_path, new_tracker).write_file()

    elif user_choice == "2":
        user_new_task_name = input("and new name is?: ")
        user_task.change_task(user_new_task_name)
        print(user_task)
    elif user_choice == "3":
        Task().del_task(user_task)
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
            TasksIO(dir_path, user_name).write_file()

        elif user_choice == "2":
            user_new_task_name = input("and new name is?: ")
            user_task.change_task(user_new_task_name)
            print(user_task)
        elif user_choice == "3":
            Task().del_task(user_task)
            exit("you task is deleted")

