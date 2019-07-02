"""Import modules..."""
from string import ascii_uppercase, ascii_lowercase, punctuation, digits
import random
import pickle
"""Print introductory text..."""
print ("""
	PasswordGenPy ver 1.0.1
	=======================
	Generate and store passwords
	============================
	Designed by Josemaria Nriagu
	(jnriagu@yahoo.com)
""")

def first_run():
	id_pass = input("Please enter a new password: ")
	rule = [lambda id_pass: any(x.isupper() for x in id_pass),
			lambda id_pass: id_pass.punctuation() == True,
			lambda id_pass: len(id_pass) < 6,
			]
	if not all(rules for rules in rule):
		print("Please read the instructions and try again")
		return first_run()

"""check for master key file"""
try:
	file = open('kmast.py', 'r+')
except FileNotFoundError:
	file_new = 'kmast.py'
if file.read(4) != 'mast':
	file.write("mast = {}")
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
	first_run()
	#file.write("\nmast.update({%s: %s})".% (name, id_pass))
	file.close()
else:
	pass
#mast.update({name: id_pass})
"""Print demarcator"""
print ("*" * 50)
print ("")
