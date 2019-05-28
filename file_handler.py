import os

class FileHandler:


    def __init__(self):
        current_working_directory = os.getcwd()
        subdirectory = "\Folders"
        destination_folder = current_working_directory + subdirectory

        try:
            os.mkdir(destination_folder)
        except FileExistsError:
            print("Složka", destination_folder ,"existuje!")

    def make_dirs(self, startno, amount):
        self.startno = startno
        self.amount = amount
        self.counter = startno
        self.new_folder_name = 000000

        # replace with string function!!!!
        for i in range(self.amount): #cykly v rámci množství složek:
            if self.counter <10:
                self.new_folder_name = "00000"+str(self.counter)
            elif self.counter <100:
                self.new_folder_name = "0000"+str(self.counter)
            elif self.counter <1000:
                self.new_folder_name = "000"+str(self.counter)
            elif self.counter <10000:
                self.new_folder_name = "00"+str(self.counter)
            elif self.counter <100000:
                self.new_folder_name = "0"+str(self.counter)
            else:
                self.new_folder_name = str(self.counter)

            self.counter += 1   # increment

            print(self.new_folder_name)

