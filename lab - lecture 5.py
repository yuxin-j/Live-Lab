# 1: This code does not run!  Try it and examine the errors, then figure out 
# what needs to be changed to make it work.

a = 10

def first_func(b=20):
    c = 30
    value = second_func()
    return a + b + c + value

def second_func(d=40):
    e = 50
    return d + e

result = first_func()


# 2: Take this code from the last lab and write a function so that the form of
# the final answer is:
# answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
# Turn it into {'Noah': datetime(1999, 2, 23),
#               'Sarah':datetime(2001, 9, 1),
#               'Zach': datetime(2005, 8, 8)}
# HINT: The datetime library has a function that turns strings of the right format into dates.

def convert_date(date_dict):
    
    date_format = '%m/%d/%Y'
    answer = {k.capitalize():datetime.datetime.strptime(v, date_format) for k, v in
    date_dict.items()}
    
    return answer

end_dict = convert_date(start_dict)

