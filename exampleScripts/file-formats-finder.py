

import os

# Get the list of file formats in the directory
file_formats = set(map(lambda x: x.split('.')[-1], os.listdir('/home/lilli/Documents/Java-Projects/virtual-pet-game')))

# Print all the file formats
for file_format in file_formats:
    print(file_format)