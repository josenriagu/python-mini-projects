meal_cost = raw_input ("Please enter value of meal: ")

def tax (bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print ("With tax: %f" % (bill))
    return bill

def tip (bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print ("With tip: %f" % (bill))
    return bill
    
#meal_cost = 100
if meal_cost.isdigit():
	meal_with_tax = tax(meal_cost)
	meal_with_tip = tip(meal_with_tax)
	print ("Meal with tax: %a, Meal with Tip: %a" % (meal_with_tax, meal_with_tip))
else:
	print ("Incorrect value. Enter only numbers!!")