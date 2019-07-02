from random import *

out = ['1', '2', '3', '4', '5', '6', '7']

daily = []
run = 4

while run != 0:
	a = choice(out)
	daily.append(a)
	out.remove(a)
	run = run - 1


print ('   '.join(daily))