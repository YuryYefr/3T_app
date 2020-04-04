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
    task_payment = None

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        """something readable by human"""
        return f'user_name: {self.user_name.user_name} \ntask_name:' \
            f'{self.task_name} \nstarted on: {self.start_date} \ntask describe: {self.docs}' \
            f'\nplanning_start_date: {self.planning_start_date}\nplanning_end_date: {self.planning_end_date}' \
            f'\nyour code: """{self.user_code}"""\nended: {self.end_date} \nestimated time: {self.estimated_time}' \
            f'\nduration: {self.duration}\ntask status: {self.task_status}\npayment in UAH(20$ per day): {self.task_payment}'

    def start_new_task(self, user_name):
        """starting new task"""
        self.user_name = user_name
        self.task_name = input("name your task:")
        self.start_date = dt.datetime.now()
        a_s_y = int(input("starting year"))
        a_s_m = int(input('starting month'))
        a_s_d = int(input("starting days"))
        a_e_y = int(input("ending year"))
        a_e_m = int(input("ending month"))
        a_e_d = int(input("ending days"))
        self.planning_start_date = dt.date(a_s_y, a_s_m, a_s_d)
        self.planning_end_date = dt.date(a_e_y, a_e_m, a_e_d)
        self.docs = input("describe your task")
        self.estimated_time = self.planning_end_date - self.planning_start_date
        self.task_payment = self.estimated_time.days * (20 *28)
        if dt.date.today() != self.estimated_time:
            self.task_status = "work in progress"
        else:
            self.task_status = "ended"
        return self

    def change_task(self):
        """change_name"""
        new_name = input("new name: ")
        self.task_name = new_name
        return self.task_name

    def change_user(self):
        """changing user"""
        new_name = input("new nme: ")
        self.user_name = new_name

    def change_pl_st_date(self):
        """changing planning start date"""
        a_s_y = int(input("starting year"))
        a_s_m = int(input('starting month'))
        a_s_d = int(input("starting days"))
        self.planning_start_date = dt.date(a_s_y, a_s_m, a_s_d)

    def change_pl_end_date(self):
        """changing planning end date"""
        a_e_y = int(input("ending year"))
        a_e_m = int(input("ending month"))
        a_e_d = int(input("ending days"))
        self.planning_end_date = dt.date(a_e_y, a_e_m, a_e_d)

    def change_docs(self):
        """changing docs"""
        self.docs += input("adding docs")

    def change_user_code(self):
        """changing user code"""
        self.user_code += input("adding code")

    def del_task(self):
        """delete task"""
        task = Task()
        del task
