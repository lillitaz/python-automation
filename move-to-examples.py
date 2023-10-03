

import os
import shutil

# Get current directory
current_dir = os.getcwd()

# Get list of files in current directory
files_in_dir = os.listdir(current_dir)

# Iterate over the files in the directory
for file in files_in_dir:
    # Check if the file ends with .py
    if file.endswith('.py'):
        # Check if the file is not named python-openai.py or move-to-examples.py
        if file != 'python-openai.py' and file != 'move-to-examples.py':
            # Move the file to the exampleScripts folder
            shutil.move(file, os.path.join(current_dir, 'exampleScripts'))