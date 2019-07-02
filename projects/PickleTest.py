"""import pickle

a = { "abc" : [1, 2, 3], "qwerty" : [4,5,6] }
afile = open(r'C:\a.pkl', 'wb')
pickle.dump(a, afile)
afile.close()

#reload object from file
file2 = open(r'C:\a.pkl', 'rb')
new_d = pickle.load(file2)
file2.close()

#print dictionary object loaded from file
print (new_d)"""

import TextReader
reader = TextReader(hello.txt)
reader.readline()