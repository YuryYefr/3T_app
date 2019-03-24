"""let's do some work with our tracker and tasks"""
from core_classes.main_objects.files import *
from core_classes.main_objects.task_file_ops import *
from core_classes.main_objects.tracker import Tracker


def track_control():
    """"list of trackers to select"""
    try:
        list_files()
        tracker_name = input("choose tracker")
        print("1.remove tracker\n"
              "2.change tracker name\n"
              "3.proceed to task")

        tracker = TasksIO(dir_path, tracker_name).read_file()
        user_choose = input("you choose: ")

        if user_choose == "1":
            Tracker(tracker_name).del_track(tracker_name)
            exit("your tracker has been deleted")

        elif user_choose == "2":
            return tracker.change_name(tracker_name)
        TasksIO(dir_path, tracker).write_file()
        tracker = TasksIO(dir_path, tracker_name).read_file()
        return tracker


    except Exception as e:
        print(e)


def task_control(tracker):
    """operations on task"""
    print("choose task")
    for task in tracker.task:
        print(task.task_name)
    user_choice = input("you choose: ")
    for task in tracker.task:
        if user_choice in task.task_name:
            local_task = task
            print(task.__str__())
    print("1.if you want to change task name\n"
          "2.if you want to change user name\n"
          "3. if you want to change planning_start_date\n"
          "4.if you want to change planning_end_date\n"
          "5.if you want to change docs\n"
          "6.if you want to change user code\n"
          "7.to end program")
    user_choice = input("you choose: ")
    while user_choice.isalpha():
        user_choice = input("you choose: ")
    if user_choice == '1':
        local_task.change_task()
        TasksIO(dir_path, tracker).write_file()
    elif user_choice == "2":
        local_task.change_user()
        TasksIO(dir_path, tracker).write_file()
    elif user_choice == "3":
        local_task.change_pl_st_date()
        TasksIO(dir_path, tracker).write_file()
    elif user_choice == "4":
        local_task.change_pl_end_date()
        TasksIO(dir_path, tracker).write_file()
    elif user_choice == "5":
        local_task.change_docs()
        TasksIO(dir_path, tracker).write_file()
    elif user_choice == "6":
        local_task.change_user_code()
        TasksIO(dir_path, tracker).write_file()
    else:
        exit("saving and closing")
    TasksIO(dir_path, tracker).write_file()
    exit("saving and closing")
