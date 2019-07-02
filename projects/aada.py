try:
	file = open('kmast.py', 'r+')
except:
	file = open('kmast.py', 'w')
	file.close()
# creates the first file

str = """
print ("# This is a statement inside \'kmast.py\' #")
f = open('script.py','w')
f.write(\'print(\"## and this is inside \\'script.py\\' ##\")\')
f.close()
print("script.py fired by kmast.py")
exec(open("script.py").read())
"""
file_handler = open('kmast.py', 'w')
file_handler.write(str)
file_handler.close()
print('Done')