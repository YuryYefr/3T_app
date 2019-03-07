import pickle


class TasksIO:

    def __init__(self, dir_path, task):
        """our class to work with write/read data"""
        self.dir_path = dir_path
        self.task = task

    def write_file(self):
        """writing file"""
        my_pickle_user = pickle.dumps(self.task)
        with open(self.dir_path, 'wb') as f:
            f.write(my_pickle_user)

    def read_file(self):
        """reading file"""
        with open(self.dir_path, 'rb') as f:
            task_bytes = f.read()
        unpickle_user = pickle.loads(task_bytes)
        print(unpickle_user)
