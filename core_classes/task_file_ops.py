import pickle
import os


class TasksIO:
    def __init__(self, dir_path, task):
        """our class to work with write/read data"""
        self.dir_path = dir_path
        self.task = task

    def gen_file(self, task):
        file_name = f'{task}'
        return file_name

    def write_file(self):
        """writing file"""
        file_name = self.gen_file(self.task.tracker_name)
        full_path = os.path.join(self.dir_path, file_name)
        pickled_task = pickle.dumps(self.task)
        with open(full_path, 'wb') as f:
            f.write(pickled_task)

    def read_file(self):
        """reading file"""
        full_path = os.path.join(self.dir_path, self.task)
        with open(full_path, 'rb') as f:
            self.task = f.read()
        return pickle.loads(self.task)
