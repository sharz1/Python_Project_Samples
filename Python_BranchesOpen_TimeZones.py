
'''
Python v 3.6.2

Author Sharlee Bryan

Description: A company just opened two new branches: one in New York City,
the other in London. This simple program determines whether the branches are open or
closed based on the current time of the Headquarters in Portland, OR. The hours of both
branches are 9:00AM - 9:00PM in their respective time zones.
'''


from datetime import datetime
from datetime import time

Local_Time = datetime.now().hour

#London Office Hours are 9am-9pm, which is 1am-1pm in Portland
if Local_Time >= 1 and Local_Time < 13:
    print("The London Office is currently Open")
else:
    print("The London Office is currently Closed")
    
#New York Office Hours are 9am-9pm, which is 6am-6pm in Portland
if Local_Time >= 6 and Local_Time < 18:
    print("The New York Office is currently Open")
else:
    print("The New York Office is currently Closed")
