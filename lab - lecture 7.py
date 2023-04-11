# 1. Will the code run, & if so, what will be the data types & values of a & b?
a, b = [10, 11]
# Yes, a = 10, b = 11, both int
a, b = [10]
# No
a, b = [10, 11, 12]
# No
a, *b = [10, 11]
# Yes, a = 10, b = [11]
a, *b = [10]
# Yes, a = 10, b = []
a, *b = [10, 11, 12]
# Yes, a = 10, b = [11, 12]


# 2. What data type is args & kwargs inside the function, what are the values,
# and how would you use them?
def base_function(*args, **kwargs):
    pass

base_function()
base_function(['A', 'B'])
base_function('Hello', 'World', '!')
base_function(answer=True, question='No')
base_function('a', 'b', c='value', d=10)


# 3. Write a lambda function that is passed into my_func, & performs a valid
# operation on a & b, without editing the contents of my_func at all.

def my_func(a, b, func):
    value = func(a, b)
    return value

lambda a, b: sum(a, b)