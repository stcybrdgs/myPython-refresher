#
# Example file for working with timedelta objects
# rem: use the timedelta functions from python library
# to help you perform time-based mathematics
#

# import modules from python library
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print( timedelta( days = 365, hours = 5, minutes = 1 ) )
targetTime = timedelta( hours = 5, minutes = 1 )

# print today's date
now = datetime.now()
print( "today is: " + str(now) )

# print today's date one year from now
print( "One year from now will be: " + str( now + timedelta( 365 ) ) )

# create a timedelta that uses more than one argument
print( "In two days and three weeks, it will be: " +
      str( now + timedelta( days = 2, weeks = 3 ) ) )

# calculate the date 1 week ago, formatted as a string
print( "Last week, the date was: " +
      str( now - timedelta( weeks = 1 ) ) )

# reframe previous statement with additional formatting
t = now - timedelta( weeks = 1 )
s = t.strftime( "%A %B %d, %Y" )
print( "One week ago, it was: " + s )



