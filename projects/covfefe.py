import re
def f(x,k='aeiouy])'):
	b,c,v=re.findall(f'(.*?[{k}([^{k}.*?([{k}',x)[0];
	return b+c+(('bcdfgkpstvz'+c)['pgtvkgbzdfs'.find(c)]+v)*2

print(f('coverage'))
print(f('Ezenduka'))
print(f('Sabo'))
print(f('Sancho'))
print(f('Josemaria'))
print(f('Cosmas'))