name = input ("Please Enter your name: ")

name = name.title()
print ("Hello %s, welcome to Python!!" % name)

def timestamp():
	from datetime import datetime
	now = datetime.now()
	print ("Today's date is: %a/%a/%a and current time is: %a:%a:%a \n"
               "Lol! Don't check your clock, it's correct johr!" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
	return collatz()
def collatz():
	number = input ("Please enter a valid integer: ")
	if number.isdigit():
		print ("Integer")
	else:
		print ("Your Fada!!! Integers must be a valid counting number like 1, 2, ... 50, 51 etc")
		return collatz()
	while int(number) >= 1:
		print (number)
		number = int(number) - 1
	return cont()

def cont():
	print ("Dear %s, do you want to try again?" % name)
	answer = input ("Type YES to Continue, otherwise type NO to Quit: ").lower()
	if answer == 'yes':
		print ("Ahoy! Welcome Back %a" % name)
		return timestamp()
	elif answer == 'no':
		print ("Thank you for trying! Goodbye %s!!" % name)
		quit()
	else:
		print ("Invalid Input! You don't understand grammar?! Try Again!!")
		return cont()

timestamp()
collatz()