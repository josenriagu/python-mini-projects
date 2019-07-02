def first_run():
	"""Start"""
	name = input("Please enter your name to create your master key: ").title()
	"""Print demarcator"""
	print ("*" * 50)
	print ("")
	"""Print instructions"""
	print("Hello %s, create a Master key which must:\n"
	"*. be a minimum of six (6) characters long\n"
	"*. have at least one uppercase\n"
	"*. have at least one special character" % name)
	print("")
	id_pass = input("Please enter a new password: ")
	mast.update({name: id_pass})