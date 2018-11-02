#
# Example file for working with loops
#

# define a while loop -----------------
def myWhile():
  print( "myWhile():" )

  x = 0
  while ( x < 5 ):
    print( x )
    x = x + 1

# END ... 


# define a for loop -------------------
def myFor():
  print( "myFor():" )
  
  # note: range is not inclusive of upper limit
  for x in range( 5, 10 ):
    print( x )

# END ...


# for loop over a collection ------------
def myDays():
  print( "myDays():" )
  
  days = [ "MON", "TUE", "WED", "THR", "FRI", "SAT", "SUN" ]
  for d in days:
    print ( d )

# END ...
 

# using break ---------------------------
def myBreak():
  print( "myBreak():" )

  for x in range ( 5, 10 ):
    if ( x == 7 ): break
    print( x )

# END ...


# using continue -------------------------
def myContinue():
  print( "myContinue():" ) 

  for x in range ( 5, 10 ):
    if ( x % 2 == 0 ): continue
    print( x )

# END ...


# use the enumerate() function ----------
# to get the index of each iteration 
def myEnum():
  print( "myEnum():" )  
  
  days = [ "MON", "TUE", "WED", "THR", "FRI", "SAT", "SUN" ]
  for i, d in enumerate( days ):
    print ( i, d )

# END ...

# using main to call functions ----------
def main():
  myWhile()
  myFor()
  myDays()
  myBreak()
  myContinue()
  myEnum()

# END ...

if __name__ == "__main__":
  main()
