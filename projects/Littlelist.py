def namelist():
    sur = input ("Please enter your Surname: ")
    fir = input ("Please enter your First name: ")
    mid = input ("Please eneter your Middle name: ")

    name = [sur.title(), fir.title(), mid.title()]

    print ("Your Full name is " + name[0] + " " + name [1] + " " + name [2])
    secondtrial()

def secondtrial():
    reply = input("Do you want to enter another name?(YES/NO) ")
    if reply.lower() == "yes":
        namelist()
        return secondtrial()
    elif reply.lower() == "no":        
        print ("Thank you for trying! Bye!!")
        quit()
    else:
        print ("Invalid input, please try again!!")
        return secondtrial()

namelist()
