from core_classes.task_file_ops import *
from core_classes.timer import *
from core_classes.task import *
from core_classes.tracker import Tracker



def run_prog():
    dir_path = "C:/Users/123/PycharmProjects/3T_app/storage.py"
    user_help = None
    user_name = input("what is your name?: ").capitalize()
    while user_name.isdigit():
        print("your name should be in letters")
        user_name = input("what is your name?: ").capitalize()
    admin = "yuriyefr".capitalize()
    if user_name != admin:
        NotImplementedError
    print("checking for actual trackers")
    if user_name not in dir_path:
        print('\t nothing found')
    else:
        print(f'founded {user_name} tasks in storage\n'
              f'do you want to proceed with your tracker?')
        user_choice = input("y/n: ").lower()
        if user_choice == 'y':
            NotImplementedError
        else:
            pass
    user_choice = input("do you want to start task?: y/n").lower()
    if user_choice == "n":
        exit("shutting down the program")

    elif user_choice == "y":
        user_task_name = Task()
        user_task_name.start_new_task(user_name)
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
        user_task_name.user_code = input("some code")
        stop = Time().stop_time()
        user_task_name.end_date = dt.datetime.now()
        user_task_name.duration = stop - start

        TasksIO(dir_path, user_task_name).write_file()


    elif user_choice == "2":
        user_new_task_name = input("and new name is?: ")
        user_task_name.change_task(user_new_task_name)
        print(user_task_name)
    elif user_choice == "3":
        Task().del_task(user_task_name)
        print(user_task_name)
        exit("you task is deleted")

    elif user_choice == "4":
        print(user_task_name)
        # TasksIO(dir_path, user_task_name).read_file()
