

import time
import os

# set file path to current folder
filepath = "/home/user/Documents/Python/python-automation/README.md"

# open and read the README.md file
with open(filepath,'r') as f:
    # loop through each line in the README.md file
    for line in f:
        print(line, end="")
        # add a sleep for each line
        time.sleep(1)

# close the file
f.close()