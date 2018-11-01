#
# Example file for working with date information
#


# import classes from the date/time standard modules
# in the Python library
from datetime import date
from datetime import time
from datetime import datetime


def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print( "Today's date is: ", today )

  # print out the date's individual components
  print( "Date components:", 
    today.day, 
    today.month, 
    today.year 
  )
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print( "Today's weekday number is: ", today.weekday() )
  days = [ "mon", "tue", "wed", "thr", "fri", "sat", "sun" ]
  print ( "Which is a: ", days[ today.weekday() ] )

  # retrieve tomorrow's weekday
  tomorrow = today.weekday() + 1
  print ( "Tomorrow is a: ", days[ tomorrow ] )


  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print( "The current data and time is ", today )

  # Get the current time
  t = datetime.time( datetime.now() )

# END main() ...

  
if __name__ == "__main__":
  main();
  