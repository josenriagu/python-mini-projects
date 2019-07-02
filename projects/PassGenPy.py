"""Print introductory text..."""
print ("""
	PasswordGenPy ver 1.0.1
	=======================
	Generate and Store Passwords
	============================
	Designed by Josemaria Nriagu
	(jnriagu@yahoo.com)
""")
"""Import modules..."""
import random
from string import ascii_uppercase,\
	ascii_lowercase, punctuation, digits
"""Print demarcator"""
print ("*" * 50)
print ("")

"""define functions in new file"""
signal = """
def create_new():
	name = input("Please enter your name to create your master key: ").title()
	'''Print demarcator'''
	print ("*" * 50)
	print ("")
	'''Print instructions'''
	print("Hello %s, create a Master key which must:\\n"
	"*. be a minimum of six (6) characters long\\n"
	"*. have at least one uppercase\\n"
	"*. have at least one special character" % name)
	print("")
	return first_run()
def first_run():
	id_pass = input("Please enter a new password: ")
	'''rule = [lambda id_pass: any(x.isupper() for x in id_pass),
			lambda id_pass: id_pass.punctuation() == True,
			lambda id_pass: len(id_pass) < 6,
			]'''
	if len(id_pass) < 6:
		print("Please read the instructions and try again")
		return first_run()
	mast = {}
	mast.update({name: id_pass})
	print (mast)

#mast = {}
create_new()
#mast.update({name: id_pass})
#print(mast)		
"""

"""Check for master key file"""
'''try:
	file = open('yektsm.py', 'r+')
except:'''
file = open('yektsm.py', 'w')
file.write(signal)
file.close()

exec(open('yektsm.py').read())

print ('Done')




