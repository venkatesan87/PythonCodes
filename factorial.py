def factorial(x):
    a = 1
    if x == 0:
        return a-1
    while x >= 1:
        a = a * x
        x = x - 1
    return a

num  = raw_input("Enter the number: ")
print "The factorial of %d is : %d"  %(int(num),factorial(int(num)))
