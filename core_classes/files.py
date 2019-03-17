from os import listdir
from os.path import isfile, join
from string import whitespace

def list_files():
    dir_path = 'C:/Users/123/PycharmProjects/3T_app/storage'
    onlyfiles = [i for i in listdir(dir_path) if isfile(join(dir_path, i))]
    if str(onlyfiles) == whitespace:
        print("nothing yet created")
    else:
        print("Here is the list of actual trackers" + str(onlyfiles))
