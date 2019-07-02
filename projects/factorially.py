#import module
import string
up = string.ascii_uppercase
lo = string.ascii_lowercase
pu = string.punctuation
di = string.digits

#populate morse code
morse = ['o-','-ooo','-o-o','-oo',\
		'o','oo-o','--o','oooo','oo',\
		'o---','-o-','o-oo','--','-o',\
		'---','o--o','--o-','o-o','ooo'\
		'-','oo-','ooo-','o--','-oo-',\
		'-o--','--oo']

#obtain input from user
test = input().lower()
test1 = test.split(',')
#test print
#print (up[0],morse[5])

print (test1)
#print (dir(string))