#fn to add tax to bill cost
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With 8 pct tax: %f" % bill  ## printed floating rather string %s
    return bill

#fn to add tip to taxed bill cost
def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With 15 pct tip: %f" % bill
    return bill

meal_cost = raw_input ('Enter meal cost ')
meal_with_tax = tax(int(meal_cost)) ##converting string to int using int()
meal_with_tip = tip(meal_with_tax)
