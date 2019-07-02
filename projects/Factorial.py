def factorial(x):
	if x < 0:
		return "Not obtainable for negative integers"
	elif x == 0:
		return 1
	else:
		return x * (factorial(x - 1))

print(factorial(-1))