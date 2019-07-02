#---LESSON 7: Loops and Iterations - For/While Loops---
nums = [1, 2, 3, 4, 5]

for i in (nums):
	print(i)
'''
Two important keywords for working with loops are:
Break: will completely brrak out of the loop
Continue: will move onto the next iteration of the loop
'''
for i in (nums):
	if i == 3:
		print ('Found!')
		break
	print(i)

for i in (nums):
	if i == 3:
		print ('Found!')
		continue
	print(i)

#---Loop within a loop---
for i in (nums):
	for letter in 'abc':
		print(i, letter)

#---Going through a loop for a given number of times, use
#the range() function---
for i in range(1, 11):
	print(i)

x = 0

while x < 10:
	print(x)
	x += 1

#---LESSON 8: Functions---
'''
use 'pass' keyword to leave a fuction you wish to define
later to avoid returning errors
Don't Repeat Yourself....keeping your code DRY
'return' is the final outcome of a fuction
Postional arguments must always come before the required
keyword arguments
'''
#passing arbitrary number of arguments and keyword values to a function
def students_info(*args, **kwargs):
	print(args) #returns a tuple conatainig the postional arguments
	print(kwargs) #returns a dictionary containin the keyword arguments

courses = ['Math', 'Art']
info = {'name': 'Jose', 'age': 22}

students_info('Math', 'Art', name = 'Jose', age = 22)
students_info(*courses, **info)

#Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	'''Return True for leap years, False for non-leap years.'''
	return year % 4 == 0 and (year % 100 != 4 or year % 400 == 0)

def days_in_month(year, month):
	'''Return number of days in that month of the year'''
	if not 1 <= month <= 12:
		return 'Invalid Month'
	
	if month == 2 and is_leap(year):
		return 29

	return month_days[month]

print(is_leap(2017))
print(days_in_month(2017, 5))

#---LESSON 9:Import Modules and Explore the Standard Library---

#What happens when we import a module?
#The system scans various locations as shown below
import sys

print(sys.path)