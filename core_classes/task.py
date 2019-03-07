import datetime as dt


class Task:
    task_name = None,
    user = None,
    start_date = None,
    end_date = None,
    duration = None,
    docs = ""
    user_code = ""

    def __init__(self):
        pass

    def __str__(self):
        """something readable by human"""
        return f'user_name: {self.user} \ntask_name:' \
            f'{self.task_name} \nstarted on: {self.start_date} \ntask describe: {self.docs} \nuser: {self.user} ' \
            f'\nyour code: """{self.user_code}"""\nended: {self.end_date} \nduration: {self.duration}'

    def start_new_task(self, user):
        """starting new task"""
        self.user = user
        self.task_name = input("name your task:")
        self.start_date = dt.datetime.now()
        self.docs = input("describe your task")
        result = f'{self.user}, {self.task_name}, {self.start_date}, {self.docs}, {self.user_code}'
        return result

    def change_task(self, new_name):
        """change_name"""
        self.task_name = new_name
        return self.task_name

    def del_task(self, task):
        """delete task"""
        task = Task()
        del task
