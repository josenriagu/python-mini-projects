'''
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
'''
'''
case1 = set(range(2,6))
case2 = set(range(6,21))

n = 10

if n % 2 == 1:
	print("Weird")
elif n % 2 == 0 and n in case1:
	print("Not Weird")
elif n % 2 == 0 and n in case2:
	print("Weird")
elif n % 2 == 0 and n > 20:
	print("Not Weird")

a = 4
b = 3
print(a + b)
print(abs(a - b))
print(a*b)
'''
'''
print(a//b)
print(a/b)
'''
'''
n = 5
for i in range(n):
	print(i*i)
'''
'''
def is_leap(year):
	leap = False

	if year % 400 == 0:
		leap = True
	elif year % 100 == 0:
		leap = False
	elif year % 4 == 0:
		leap = True
	return leap

print(is_leap(1988))
'''
'''
n = 10
for i in range(n+1):
	if i == 0:
		continue
	print(i, end = "")
'''
import numpy as np
'''
a = list(map(int, input().split()))
x = numpy.zeros(a, dtype=numpy.int)
y = numpy.ones(a, dtype=numpy.int)
print (x)
print (y)
'''
#print (help(numpy))
'''
a = list(map(int, input().split()))
print(numpy.eye(a[0], a[1], k = 0))
'''
'''
N, M = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(N)], int)
B = np.array([list(map(int, input().split())) for _ in range(N)], int)
print(np.add(A,B), np.subtract(A,B), np.multiply(A,B,), np.floor_divide(A,B), np.mod(A,B), np.power(A,B), sep = "\n")
'''
'''
for i in N:
list = []
list.insert(0,5)
list.insert(1,2)
list.insert(2,4)
list.insert(3,7)
print(list)
list.remove(4)
list.append(1)
list.append(6)
list.sort()
print(list)
list.pop()
list.reverse()
print(list)
'''
'''
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)
'''
'''
def factorial(x):
  init = 1
  if x < 0:
    print("Sorry, factorial does not exist for negative numbers")
  elif num == 0:
    print("The factorial of 0 is 1")
  else:
    for i in range(init, x + init):
       factorial *= i
       print("The factorial of %s is %s" % x, factorial)
       '''
def is_prime(x):
	if x == 0:
		return False
	if x == 1 or x == 2 or x == 3:
		return True
	else:
		for _ in range (1,x-1):
			if x % _ == 0:
				return False
			else:
				return True

print(is_prime(5))