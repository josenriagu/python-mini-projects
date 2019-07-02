def hotel_cost(night):
	print ("You will pay a total of N%a for %a nights" % (400 * int(night), night))
	if int(night) >= 5:
		print ("Boy! you no get house? Jesu!!!")
	else:
		print ("Smart Spender!!")

a = input("Please enter the number of nights spent: ")
if a.isdigit():
	totalcost = hotel_cost(a)
	print (totalcost)
else:
	print("Error! Enter only numbers mumu!")