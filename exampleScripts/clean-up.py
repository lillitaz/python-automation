

import os

# create new folder "old-downloads"
os.mkdir("/home/lilli/old-downloads")

# get list of all files in /home/lilli/Downloads
files = os.listdir("/home/lilli/Downloads")

# loop through each file and move it to "old-downloads" folder
for file in files:
    # get full path of file
    file_path = os.path.join("/home/lilli/Downloads", file)
    # move file to "old-downloads" folder
    os.rename(file_path, "/home/lilli/old-downloads/" + file)