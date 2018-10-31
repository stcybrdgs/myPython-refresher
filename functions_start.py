#
# Example file for working with functions
#


# define a basic function
def func1():
    x = 1 + 1 
    print("I am a function.")
    print("1 + 1 = ", x)

func1()


# function that takes arguments
def func2(x):
    print("I am a function.")
    print("1 + 1 = ", x)

func2(2)


# function that returns a value
def add(a,b):
    x = a + b
    return x

print(add(1,2))


# function with default value for an argument
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result        

print(power(2))
print(power(2,3))
print(power(3,4))

# if you specify the var in the arg list, 
# Python is agnostic to their order
print(power(x=4, num=3)) 
print(power(num=3, x=4))


# function with variable number of arguments -------------
# The * means that a variable number of args is accepted,
# so if there is more than one, then Python will loop 
# through each one and combine them in the final result.
# Keep in mind that you can combins a variabe arg list
# within a set of formal arguments, but the variable arg list
# will always have to be the last parameter
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(2,4,6))    

