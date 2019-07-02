mast = {}
name = 'Jose'
id_pass = 'esjsohfbe'
mast.update({name: id_pass})

print(mast)
def first_run():
	id_pass = input("Please enter a new password: ")
	'''rule = [lambda id_pass: any(x.isupper() for x in id_pass),
			lambda id_pass: id_pass.punctuation() == True,
			lambda id_pass: len(id_pass) < 6,
			]'''
	if len(id_pass) < 6:
		print("Please read the instructions and try again")
		return first_run()
exec(first_run())