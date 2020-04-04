from string import whitespace
from core_classes.main_objects.task_file_ops import *

dir_path = 'C:/Users/123/PycharmProjects/3T_app/storage'


def list_files():
    """listing trackers"""
    onlyfiles = [i for i in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, i))]
    if onlyfiles == whitespace:
        print("nothing yet created")
    else:
        print("Here is the list of actual trackers" + str(onlyfiles))
    return onlyfiles


def data_retrieve(tracker):
    """retrieving and numerating trackers"""
    trackers = TasksIO(dir_path, tracker).read_file()
    for task, number_of_task in enumerate(trackers.task, 1):
        print(task, number_of_task)
