from string import ascii_letters, whitespace
from random import choice as ch
import os


class Tracker:
    tracker_name = ""
    tracker_describe = ""
    dir_path = 'C:/Users/123/PycharmProjects/3T_app/storage'

    def __init__(self, task=None):
        self.task = task

    def start_track(self, user_name, task):
        """method that creates tracker"""
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
        """readable by human"""
        return f'{self.tracker_name}\n {self.tracker_describe} \n{self.task}'

    def del_track(self, task):
        """method to delete task"""
        os.remove(f'C:/Users/123/PycharmProjects/3T_app/storage/{task}')

    def change_name(self, track):
        """method to change track name"""
        new_track = input("new track name")
        os.chdir('C:/Users/123/PycharmProjects/3T_app/storage')
        os.rename(track, new_track)
        self.tracker_name = new_track
        return self
