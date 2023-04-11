# Fix the problems with each of these classes (1-3).

# 1
class MyClass():
    def __init__(self, a, b):
        self.a = 10
        self.b = 20
        self.x = a + b
my_instance = MyClass(1, 2)
my_instance.x

# 2
class MyClass():
    a = 10
    b = 20
    x = a + b
my_instance = MyClass()
my_instance.x

# 3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

# 4 A Fibonacci sequence is a list of values where each is the sum of the 
# previous two, e.g. [0, 1, 1, 2, 3].
#      - First write a function that takes in a list of any two values, then
#        calculates the rest of the sequence starting from that point.  It
#        should have two arguments:  the starting list and the number of 
#        additional Fibonacci sequence elements to calculate.
#      - Second, turn this into a class that takes the same list at start,
#        but has a method that takes only the number of additional Fibonacci 
#        sequence elements as an argument and then calculates the sequence.
#  Note that technically the Fibonacci sequence starts at 0, but for our
#  coding practice we can calculate it from any two starting values.

def fib(start_list, num):
    
    for i in range(len(start_list)+1):
        if i <= num:
            
            result = start_list[i] + start_list[i+1]
            start_list.append(result)
    
    return start_list

final_list = fib([0,1], 5)


class FibSeq():
    
    def __init__(self, start_list):
        
        self.start_list = start_list
        
    def cal(self, num):
        
        for i in range(len(self.start_list)+1):
            if i <= num:
                
                result = self.start_list[i] + self.start_list[i+1]
                self.start_list.append(result)
        
        return self.start_list

new_final_list = FibSeq([0,1])
new_final_list.cal(5)
    
        
    
