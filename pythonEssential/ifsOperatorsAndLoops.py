# python examples of
# if-elif-else
# operators
# loops

# if-elif-else =========================
print('\nif-elif-else example: ==========')
if True:
    print('if true')
elif False:
    print('elif true')
else:
    print('not true')

# operators ============================	
# comparison operators:
#    a == b        equal
#    a != b        not equal
#    a < b         less than
#    a > b         greater than
#    a <= b        less than or equal
#    a >= b        greater than or equal
#    
# logical operators:
# 
#    a and b       true if both a and b
#    a or b        true if x or b
#    not a         inverse state
#    
# identity operators:
#    a is b        true if the same object
#    a is not b    true if not the same object
#    
# membership operators:
#    a in b        true if z member of collection b
#    a not in b    true if z not member of collection b
#
# arithmetic operators:
#    +             addition
#    -             subtraction
#    *             multiplication
#    /             division
#    //            integer division
#    %             remainder (ie, modulus)
#    **            exponent
#    -             unary negative
#    +             unary positive
#
# bitwise operators:
#    &             and
#    |             or
#    ^             xor
#    <<            shift left
#    >>            shift right

# ternary operator (as of python 2.5) ==================
print('\nternary operator example: ==========')
sleepy = 0
x = 'Go to sleep.' if sleepy else 'Stay up.'
print('when sleepy is false:', x)
sleepy = 1
x = 'Go to sleep.' if sleepy else 'Stay up.'
print('when sleepy is true: ', x)

# bitwise operator example ===================
print('\nbitwise operator example: ==========')
def printBits(x, y, z):
	print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
	print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
	
print('the AND operator & :')
print('(if x bit and y bit then z bit)')
x, y = 0x0a, 0x02
z = x & y
printBits(x, y, z)

print('\nthe OR operator | :')
print('(if x bit or y bit then z bit)')
x, y = 0x0a, 0x05
z = x | y
printBits(x, y, z)

print('\nthe XOR operator ^ :')
print('(if bit or y bit but not both then z bit (ie, flip the bits))')
x, y = 0x0a, 0x0f
z = x ^ y
printBits(x, y, z)

print('\nthe shift left operator <<:')
x, y = 0x0a, 0x01
z = x << y
printBits(x, y, z)

print('\nthe shift right operator >>:')
x, y = 0x0a, 0x01
z = x >> y
printBits(x, y, z)