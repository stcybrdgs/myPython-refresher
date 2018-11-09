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
#
# boolean operators:
#    and           and
#    or            or
#    not           not
#    in            value in set
#    not in        value not in set
#    is            same object identity  
#    is not        not same object identity
#
# operator precedence:
# (rem order in which operators are evaluated in compound expressions)
#    exponent                **
#    pos, neg                +x, -x
#    mult, div, remainder    *, /, //, %
#    add, subtract           +, -
#    bitwise shift           <<, >>
#    bitwise AND             &
#    bitwise XOR             ^
#    bitwise OR              |
#    comparisons             in, not in, is, is not, <, <=, >, >=, !=, ==
#    boolean NOT             not x
#    boolean AND             and
#    boolean OR              or


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

# loops ==============================================
# python has two basic forms of loops: while and for
# while: uses a condition and executes loop while condition is true
# for:   uses a sequence with a counter and executes until sequence terminates
#
# while loop example:
print('\nwhile loop example (try cookie): =============')
password = 'cookie'
pw = ''
while pw != password:
    pw = input("What's the password? ")
print('that is correct!')
#
# for loop example:
print('\nfor loop example: =============')
books = ('comic book', 'text book', 'picture book')
for book in books:
	print(book)
	
# additional loop controls
# rem you can further control loops with continue, else, and break
# continue    shortcuts current loop iteration and starts the next iteration
# break       terminate the loop
# else        executes if loop ends normally, won't run if break occurs
print('\nwhile loop example with additional controls')
print('try swordfish =============')
secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count = count + 1
    if count > max_attempt: break
    if count == 3: continue
    pw = input( '{}: What is the secret word? '.format(count) )
else:
    auth = True
	
print('Authorized' if auth else 'Unable to authorize')
skills = [ 'Staffing', 'Training', 'Operations', 'P&L', 'Cheer Leading' ]