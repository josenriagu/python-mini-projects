#---LESSON 5: Dictionaries - Working
#with Key-Value Pairs---

student = {'name': 'Jose', 'age': 22, 'courses': ['Math', 'Communications']}

print(student)
print(student['name'])
print(student['courses'])

'''
Dictionaries can contain any immutable data type
as key or value. Accessing a key that doesn't exist
results in a KeyError
'''
#---Overiding KeyErrors (using the get() function)---

print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

#--Updating values using direct assignment---

student['phone'] = '555-5555' #adds a new Key-Value pair
student['name'] = 'Jane' #changes the existing value for the given key

print(student)

#---Updating values using update() function---

student.update({'name': 'Val', 'age': 26, 'phone': '555-5555'})
print(student)
#print(dir(student))

#--- deleting values from a dictionary---
del student['age']
phone = student.pop('phone')

print(student)
print(phone) #shows the poppped value saved in 'phone' variable

#---Want to know the number of keys in a dict?---
print(len(student))
print(student.keys()) #shows the keys
print(student.values()) #shows the values
print(student.items()) #shows the keys and values

#--Looping through dictionaries--
for key in student:
	print(key)

for key,value in student.items():
#"for key,value in student:" will return a ValueError
	print(key, value)

#---LESSON 6: Conditionals and Boolean - If, Else
#and Elif Statements---

if True:
	print('Conditional was True')
if False:
	print('Conditional was True') #doesn't evaluate

language = 'Python'

if language == 'Python':
	print('Conditional was True')
'''
Comparisons:
Equal:----------------==
Not Equal:------------!=
Greater Than:--------->
Less Than:------------<
Greater or Equal:----->=
Less or Equal:--------<=
Object Identity:------is

'Object identity' is used for keyword check ie
to check if values have the same id

False Values:
	False
	None
	Zero of any numeric type
	Any Empty sequence, e.g., '', (), [].
	Any empty mapping, e.g., {}

Boolean Operators:
	and
	or
	not
'''
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

if not logged_in:
	print('Please Log In')
else:
	print('Welcome')
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a==b)
print(a is b) #evaluates to False since they do not have same memory address as can ba seen below
print(a is c)

#---Print memory locations of the objects---
print(id(a))
print(id(c))
print(id(b))
'''
'is' operator like in (a is b) is synonymous to
id(a) == id(b) check behind the scene
'''
