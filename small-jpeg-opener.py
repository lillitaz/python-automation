

import os

# set path to Pictures folder
path = "/home/lilli/Pictures/Screenshots"

# initialize variables for smallest file size and file name
smallest_size = None
smallest_file = None

# loop through all files in the folder
for file in os.listdir(path):
    # check if file is a .jpeg
    if file.endswith(".jpg"):
        # get file size
        size = os.path.getsize(os.path.join(path, file))
        # check if smallest_size is None or if current size is smaller
        if smallest_size is None or size < smallest_size:
            # update smallest_size and smallest_file
            smallest_size = size
            smallest_file = file

# check if smallest_file is not None
if smallest_file:
    # open the smallest file
    os.system("xdg-open " + os.path.join(path, smallest_file))