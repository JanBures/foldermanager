"""
    Class producing sequences of empty folders numbered
    mainly from 000000 to 999999.
Methods:
    - filehandler.setsubdir changes main subdir whitch contains newly made folders
    - filehandler.makedirs initiate making of directories
    """

import os

class FileHandler:

    def __init__(self):
        self.subdirectory = "dirs"

    def get_dirs_names(self, startno, amount):
        """
        Produces list of names of folders to be created
        :param startno: start number of first directory
        :param amount: amount of folders to be created
        :return: list with names of directories
        """
        self.startno = startno if startno else 1
        self.amount = amount if amount else 10
        self.counter = startno if startno else 1
        self.new_folder_name = 000000
        self.names = []

        # replace with string function!!!!
        for i in range(self.amount):  # cykly v rámci množství složek:
            if self.counter < 10:
                self.new_folder_name = "00000" + str(self.counter)
            elif self.counter < 100:
                self.new_folder_name = "0000" + str(self.counter)
            elif self.counter < 1000:
                self.new_folder_name = "000" + str(self.counter)
            elif self.counter < 10000:
                self.new_folder_name = "00" + str(self.counter)
            elif self.counter < 100000:
                self.new_folder_name = "0" + str(self.counter)
            else:
                self.new_folder_name = str(self.counter)
            self.counter += 1  # increment
            self.final_path = str(self.get_working_dir()) +"\\"+ self.get_subdir() +"\\"+ str(self.new_folder_name)
            self.names.append(self.final_path)  # add one by one directory name into the list
        return self.names

    def make_subdir(self):
        """
        internal function creating base subdirectories
        """
        try:
            os.mkdir(self.subdirectory) # create defined subdirectory
        except FileExistsError:         # raised when directory exists
            print("Folder", self.subdirectory ,"already exists!")


    def make_dirs(self, startno, amount):
        """
        method creating directories
        :param startno:
        :param amount:
        :return:
        """
        self.make_subdir()  # create base subfolder
        dirs = self.get_dirs_names(startno, amount) # get all new dir names into a list
        for d in dirs:
            print(d)
            try:
                os.mkdir(d) # make final dirs
            except FileExistsError:
                print("Directory" , d , "exists!")

    def get_working_dir(self):
        """
        internal getter of working directory (location of script)
        :return: string path to root working directory
        """
        current_working_directory = os.getcwd()
        return current_working_directory

    def get_subdir(self):
        """
        internal getter of subdirectory name
        :return:
        """
        return self.subdirectory

    def set_subdir(self, param):
        """
        setter of subdirectory name
        :param param: string name of main subdirectory
        :return:
        """
        self.subdirectory = param

