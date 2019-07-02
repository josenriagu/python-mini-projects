import numpy
'''
a = input()
b = list(map(int, a.split()))
x = numpy.zeros(b, dtype=numpy.int)
y = numpy.ones(b, dtype=numpy.int)
print (x)
print (y)
'''
print(numpy.identity(3))
n = int(input())
m = int(input())
print(numpy.eye(n, m, k = 0))