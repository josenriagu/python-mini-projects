"""Import modules..."""
from string import ascii_uppercase, ascii_lowercase, punctuation, digits
import random

"""Introductory text..."""
print("""
    PasswordGenPy ver 1.0.1
    =======================
    Generate and store passwords
    ============================
    Designed by Josemaria Nriagu
    (jnriagu@yahoo.com)
""")
"""Print demarcator"""
print("*" * 50)
print("")

"""Functions Definitions"""
def sscrmbl(max = 24, chars =ascii_uppercase + ascii_lowercase + digits + punctuation):
    print ("Generated Password is:\n %s" % (''.join(random.SystemRandom().choice(chars) for _ in range(max))))
    print("")
    return rsp()

def rsp():
    response = input("Do you want to save this password?(Enter Yes or No):\n").lower()
    print("")
    if response == "yes":
        print ("Please wait while we save it for you")
        return nxt()
    elif response == "no":
        print ("Thank you for trying")
        print("")
        return nxt()
    else:
        print("Please try again!")
        return rsp()

def nxt():
    next_pass = input("Do you want to generate another password?(Enter Yes or No):\n").lower()
    print("")
    if next_pass == "yes":
        print("")
        return sscrmbl()
    elif next_pass == "no":
        print("")
        print("Goodbye!!")
        return quit()
    else:
        print("Please try again")
        return nxt()

def kkey():
    key = input("Enter a Master key:\n")
    """We are set to use the string module. Since we have imported only some specified functions,
    we simply go ahead and use them as they are. Note that if we had imported *all of* string module,
    we will need to call the functions with the syntax 'string.function_name'
    """
    if len(set(ascii_uppercase).intersection(key)) > 0 \
        and len(set(punctuation).intersection(key)) > 0 \
        and len(set(digits).intersection(key)) > 0 \
        and len(key) >= 6:
        print ("Valid")
        """user = {"user":name, "key":key }
        print (user)"""
        return sscrmbl()
    else:
        print("Please check the instructions and try again")
        #print("")
        return kkey()

"""Start"""
name = input("Please enter your name to create your master key:\n").title()
"""Print demarcator"""
print("*" * 50)
print("")

"""Instructions"""
print("Hello %s, create a Master key which must:\n"
    "*. be a minimum of six (6) characters long\n"
    "*. have at least one uppercase\n"
    "*. have at least one number\n"
    "*. have at least one special character" % name)
print("")
kkey()
