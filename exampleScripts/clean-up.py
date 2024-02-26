

import os

# create new folder "old-downloads"
os.mkdir("/home/user/old-downloads")

# get list of all files in your download folder
files = os.listdir("home/user/Downloads")

# loop through each file and move it to "old-downloads" folder
for file in files:
    # get full path of file
    file_path = os.path.join("/home/user/Downloads", file)
    # move file to "old-downloads" folder
    os.rename(file_path, "/home/user/old-downloads/" + file)