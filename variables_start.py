# 
# Example file for variables
#

# Declare a variable and initialize it
f=10
print(f)

# # re-declaring the variable works
f="abc"
print(f)

# # ERROR: variables of different types cannot be combined
print("this is a string" + str( 123))

# return variable from function
def someFunction(r):
    x = str(r)  + " def"
    return x

print(someFunction(1)) 

# Global vs. local variables in functions
def someOtherFunction():
    global f
    f="def"
    print(f)

print(someFunction(2))
print(f)
someOtherFunction()
print(f)


