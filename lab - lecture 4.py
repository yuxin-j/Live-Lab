#Convert these objects!

#1
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]

new_list = []

for sub_list in start_list:
    
    for num in sub_list:
        if num % 2 == 0:
            new_list.append(int(num / 2))

#2
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}

from datetime import datetime

for key in start_dict.keys():
    start_dict[key] = datetime.strptime(start_dict[key], '%m/%d/%Y')
