#### Fix the following errors (in 1-6)!

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list[my_list_len - 1])

#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
z += 'd'
print(z)

#5 Why does the x not display 10, followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
color = 'My favorite color is {}, what is yours?'.format('blue')
print(color)

#### Answer the following questions without changing the code given

#7 Make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools_unique = set(schools)
print(schools_unique)

#8 Change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals_list = list(animals)
animals_list[2] = 'cat'
print(animals_list)

#9 Make this string take a name based on a variable (you can modify the code on this one)
name = 'Carlos'
welcome = 'Hello {}, and welcome to Data and Programming!'.format(name)
print(welcome)

#10 Separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'
my_sent_low = my_sent.lower()
my_sent_list = list(my_sent_low.split(' '))
print(my_sent_list)
