#Corey Schafer Video Tutorials

#---LESSON 1: Setup and Installation---

#---LESSON 2: Introduction and Strings---
message = "Hello World"
new_message = message.replace('World', 'Universe')

greeting = 'Hello'
name = 'Jose'

message1 = greeting + ', ' + name + '. Welcome!'

#---Using formatters---
message2 = '{}, {}. Welcome!'.format(greeting, name)

#---"f-string" direct formatting---
message3 = f'{greeting}, {name.upper()}. Welcome!'
print(message)
print(len(message))
print(message[0])
print(message[6: ])

#---Some String Methods---
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World'))
print(message.find('Universe'))

print(new_message)
print(message1)
print(message2)
print(message3)

#---see the available methods for the data type---
print(dir(name))

#---Print help list for a given data type or a
#specified method in a given data type---
print(help(str))
print(help(str.lower))

#---LESSON 3: Integer and Floats---
num = 3.14 

#---see the type association of the object---
print(type(num))

num += 1

print(round(num))
print(round(num, 1))
print(round(num, 2))
'''Casting allows for explicit conversion of different
data types in Python eg num = str(num)
or num = int(num)
'''

#---LESSON 4: Lists, Tuples, and Sets---
courses = ['History', 'Math', 'Physics', 'CompSci']
courses1 = ['Geography', 'Igbo', 'Religion']

print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[::2])
print(courses[-1])

#---Some List Methods (lists are mutable)---
courses1.insert(0, 'Art')
print(courses1)

courses.append('Government')
print(courses)

courses.extend(courses1)
print(courses)

#---see the available methods for the data type---
#print(dir(courses))
  
'''sort() method sorts a list in ascending order for
numerical values or alphabetically for strings.
Use sort(reverse=True) for a descending order sorted list
Use sorted() to get a sorted version of a list without
altering the list itself'''

print(sorted(courses))

courses.sort(reverse=True)
print(courses)

#---Looping through lists---
for i in courses:
	print(i)

print("")

for i, j in enumerate(courses):
	print(i, j)

print ("")

for i, j in enumerate(courses, start = 1):
	print(i, j)

food = ['rice', 'beans', 'potato', 'garri']

food1 = ' -  '.join(food)
food2 = food1.split(' - ')
print(food1)
print(food2)

#---Tuples are immutable ie they cannot be modified---
'''
#mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print (list_1)
print (list_2)

list_1[0] = 'Art'

print (list_1)
print (list_2)

#Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print (tuple_1)
print (tuple_2)

tuple_1[0] = 'Art'
#This will result in a TypeError

print (tuple_1)
print (tuple_2)
'''

#---Sets are values that are unordered and also have
#no duplicates---
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

'''
#Empty Lists
empty_list = []
empty_lst = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Set
empty_set = {} #This isn't right! It's a Dict
empty_set = set()
'''