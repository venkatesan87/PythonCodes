'''A simple program to reverse a string'''
def reverse(a):
    length = len(a) #4
    b=[]  ## creating a list and adding elements to list
    while length > 0:
        b.append(a[length-1])
        length -= 1
    c = "".join(b)
    return c
str1 = raw_input("Enter the string to Reverse: ")
print reverse(str1)
