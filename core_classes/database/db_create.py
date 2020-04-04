import sqlite3
import pprint
from core_classes.main_objects.task_file_ops import *


def task_list():
    """creating list of our tasks in tracker"""
    result = []
    user_input = input("tracker name")
    trackers = TasksIO(dir_path='C:/Users/123/PycharmProjects/3T_app/storage', task=user_input).read_file()
    for task in trackers.task:
        result.append(task.__str__())
    return result


def db():
    """creating our table from list of tasks"""
    try:
        os.remove('C:/Users/123/PycharmProjects/3T_app/core_classes/trackers')
        conn = sqlite3.connect('trackers')
        tracker = task_list()
        c = conn.cursor()
        id_name = 1
        c.execute("CREATE TABLE tracker_task(id INT, task TEXT)")
        for v in tracker:
            c.execute("""INSERT INTO tracker_task(ID, task) VALUES(?,?)""", (id_name, v))
            id_name += 1
        conn.commit()
        for r in c.execute("SELECT * FROM tracker_task ORDER BY id "):
            pprint.pprint(r)
    except Exception as e:
        print(e)
