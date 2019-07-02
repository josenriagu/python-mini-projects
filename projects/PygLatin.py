pyg = 'ay'
print ("""Welcome to PygLatin!
This program will play with whatever word you entered!
""")

salt = input("Enter any word you like: ")
salt = salt.lower()
if salt:
    first = salt [0]
else:
    print ("Your Fada!!!, I said in lower letters!!")
#print word [1:] + first + pyg
new_word = salt + first + pyg
new_word = new_word [1:len(new_word)]
print ("PygLatin played with your word and returned %s" % new_word)
