def is_leap():
	yr = int(input())

	a = "%s is a leap year" % yr
	b = "%s is not a Leap year" % yr
	
	if yr % 400 == 0:
		return a
	elif yr % 100 == 0:
		return b
	elif yr % 4 == 0:
		return a
	else:
		return b

print(is_leap())