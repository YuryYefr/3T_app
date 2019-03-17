#TBA
class Project:
    """here our project object creates"""
    user_num = int
    tasks = []

    def __init__(self, proj_name, start_date, end_date, time_value):
        self.proj_name = proj_name
        self.start_date = start_date
        self.end_date = end_date
        self.time_value = time_value
