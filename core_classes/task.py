import datetime as dt


class Task:
    task_name = None,
    user_name = None,
    planning_start_date = None
    planning_end_date = None
    estimated_time = None
    start_date = None,
    end_date = None,
    duration = None,
    docs = ""
    user_code = ""
    task_status = None

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        """something readable by human"""
        return f'user_name: {self.user_name} \ntask_name:' \
            f'{self.task_name} \nstarted on: {self.start_date} \ntask describe: {self.docs}' \
            f'\nplanning_start_date: {self.planning_start_date}\nplanning_end_date: {self.planning_end_date}' \
            f' \nuser: {self.user_name} '\
            f'\nyour code: """{self.user_code}"""\nended: {self.end_date} \nestimated time: {self.estimated_time}' \
            f'\nduration: {self.duration}\ntask status: {self.task_status}'

    def start_new_task(self, user_name):
        """starting new task"""
        self.user_name = user_name
        self.task_name = input("name your task:")
        self.start_date = dt.datetime.now()
        a_s_y = int(input("year"))
        a_s_m = int(input('month'))
        a_s_d = int(input("days"))
        a_e_y = int(input("year"))
        a_e_m = int(input("month"))
        a_e_d = int(input("days"))
        self.planning_start_date = dt.date(a_s_y, a_s_m, a_s_d)
        self.planning_end_date = dt.date(a_e_y, a_e_m, a_e_d)
        self.docs = input("describe your task")
        self.estimated_time = self.planning_end_date - self.planning_start_date
        if dt.date.today() != self.estimated_time:
            self.task_status = "work in progress"
        else:
            self.task_status = "ended"
        return self

    def change_task(self, new_name):
        """change_name"""
        self.task_name = new_name
        return self.task_name

    def del_task(self, task):
        """delete task"""
        task = Task()
        del task
