'''from datetime import datetime

jose = datetime.now()

print ("This is a modified code!")
print ('%s/%s/%s %s:%s:%s' % (jose.day, jose.month, jose.year, jose.hour, jose.minute, jose.second))
'''
def collatz():
    number = input("Please enter a VALID integer and hit \"Enter\": ")
    if number.isdigit():
        int(number)
        print("Integer")
        
    else:
        print("Integers must be a counting number like 1, 2, ... 50, 51 etc")
        collatz()
        
    while int(number) >= 1:
        print (number)
        number = int(number) - 1

collatz()
