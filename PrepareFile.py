import os
# from tkinter import Tk
from tkinter.filedialog import askdirectory

path = ''


class File:  # Makes my life easier and the code cleaner
    def __init__(self, path: str, root=''):
        tupp = os.path.splitext(path)
        self.path = root + '/' + path
        self.filename = tupp[0]
        self.ext = tupp[1]


def create_folder(name: str, path: str):
    folder_path = path + "/" + name
    os.mkdir(folder_path)


def make_folders():
    path = askdirectory(title='Select Folder to be organised')  # Shows OS dialog box and return the path (poate pusca pe MacOS)
    folder_dict = check_folders(path)
    for folder in folder_dict.keys():
        if folder_dict[folder] == False:
            create_folder(folder, path)


def check_folders(path):
    folder_dict = {'Documents': False, 'Pictures': False, 'Videos': False, 'Zips': False, 'Apps': False}
    for dirname in os.listdir(path):
        selected_file = File(dirname, path)
        if selected_file.ext == '':  # Folders have no extension
            if selected_file.filename in folder_dict.keys():
                folder_dict[selected_file.filename] = True

    return folder_dict


make_folders()
