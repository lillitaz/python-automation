

import os

info = os.popen('df -h').read()

print(info)