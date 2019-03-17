from string import ascii_letters, whitespace
from random import choice as ch
from os import remove


class Tracker:
    tracker_name = ""
    tracker_describe = ""
    dir_path = 'C:/Users/123/PycharmProjects/3T_app/storage'

    def __init__(self, task):
        self.task = task

    def start_track(self, user_name, task):
        self.tracker_name = input("name your tracker: ")
        if self.tracker_name == whitespace:
            choices = ascii_letters
            self.tracker_name = ch(choices).strip(str=4)
            return self.tracker_name
        else:
            pass
        self.task = task
        self.tracker_describe = input("describe your tracker: ")
        return self

    def __str__(self):
        return f'{self.tracker_name}\n {self.tracker_describe} \n{self.task}'

    def del_track(self, task):
        remove(task)

    def change_name(self, track):
        self.tracker_name = track
