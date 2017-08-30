'''
Python v 3.6.2

Author: Sharlee Bryan

Description: A company's users create or edit a collection of text files
throughout the day. These text files represent data about customer orders.
Once per day, any files that are new or edited within the last 24 hours
must be sent to the home office. To facilitate this, these new or updated
files are copied to a specific 'destination' folder on a computer, so that
a file transfer program can grab them and transfer them to the home office.

The process of figuring out which files are new or recently edited and
copying them to the 'destination' folder was being done manually, which was
very expensive in terms of manpower. This script automates this task.
'''

import shutil
import os
from datetime import datetime
from datetime import time
from datetime import timedelta

Current_Time = datetime.now()
Minus24 = Current_Time - timedelta(hours=24)

source = os.path.normpath("C:/Users/singi/Desktop/SourceFilesFolder/")
sourcelist = os.listdir(source)
destination = os.path.normpath("C:/Users/singi/Desktop/TransferredFilesFolder/")

for file in sourcelist:
    Modified_Time = datetime.fromtimestamp(os.path.getmtime(source + "\\" + file))
    if Modified_Time > Minus24:
        shutil.copy(source + "\\" + file, destination)
