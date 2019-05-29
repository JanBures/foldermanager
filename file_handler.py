import os

class FileHandler:

    def __init__(self):
        self.current_working_directory = os.getcwd()
        self.subdirectory = "\Folders"
        self.destination_folder = self.get_working_dir() + self.subdirectory
        try:
            os.mkdir(self.destination_folder)
        except FileExistsError:
            print("Folder", self.destination_folder ,"already exists!")

    def get_dirs_names(self, startno, amount):
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
            self.final_path = "".join([self.get_working_dir(), "\\", self.new_folder_name]) # concatenate path

            self.names.append(self.final_path)
        return self.names


    def make_dirs(self, startno, amount):
        dirs = self.get_dirs_names(startno, amount)
        for d in dirs:
            print(d)
            try:
                os.mkdir(d)
            except FileExistsError:
                print("folder" , d , "exists!")

    def get_working_dir(self):
        current_working_directory = os.getcwd()
        return current_working_directory

    def set_dir(self, param):
        self.subdirectory = param
