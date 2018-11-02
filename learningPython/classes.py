#
# Example file for working with classes
#


# define a class with two methods -----------
class myClass():
  # rem: self = this
  def method1( self ):
    print( "myClass method1" )

  def method2( self, someString ):
    print( "myClass method2 " + someString )

# END ...


# define a class with two methods -----------
# and inherit from myClass()
class myClassChild( myClass ):
  # rem: self = this
  def method1( self ):
    myClass.method1( self )
    print( "myClassChild method1" )

  def method2( self, someString ):
    print( "myClassChild method2")

# END ...


# use main to create class objects ----------
# and call class methods
def main():
  c = myClass()
  c.method1()
  c.method2( "This is a string" )

  c2 = myClassChild()
  c2.method1()
  c2.method2( "This is a string" )

# END ...
  

if __name__ == "__main__":
  main()
