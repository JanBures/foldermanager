import file_handler

debug = 0

fh = file_handler.FileHandler()
fh.set_subdir("Vzorování")  # defines name of subfolder
fh.make_dirs(600, 10)  # creates folders 000600 to 000609
