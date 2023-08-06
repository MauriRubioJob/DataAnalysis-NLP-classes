import os
import datetime


# os.mkdir()    make directory
# os.mkdir("output_folder")


# os.listdir()
# files = os.listdir("output_folder")
# print(files)


# os.rename()
# os.rename("not_my_file.txt", "output_folder/not_my_file.txt")


# os.remove() / os.rmdir()
# os.rmdir("output_folder/New folder")


# os.stat()
stats = os.stat("output_folder/not_my_file.txt")

created_timestamp = stats.st_ctime
modified_timestamp = stats.st_mtime

time = datetime.datetime.fromtimestamp(modified_timestamp)
print(time)
