#
# Example file for formatting time and date output
#

# import datetime modules from python library
from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  print( now )


  #### Date Formatting ####
  
  # %y/%Y - Year
  print( now.strftime( "The current year is: %Y" ) )

  # %a/%A - weekday
  print( now.strftime( "The current day is: %A" ) )

  # %b/%B - month
  print( now.strftime( "The current month is: %B" ) )

  # %y, %Y, %a, %A, %b, %B, %d, %D
  print( now.strftime( "The current date is: %a, %d %B, %Y" ) )

  print( now.strftime( "%y, %Y, %a, %A, %b, %B, %d, %D" ) )

  # %c - locale date and time
  print( now.strftime( "Locale date and time: %c" ))
  
  # %x - locale date, %X locale time
  print( now.strftime( "Locale date: %x" ) )
  print( now.strftime( "Locale time: %X" ) )


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime( "Current time: %I:%M:%S %p" ))
  print(now.strftime( "24-hour time: %H:%M" ))


  ### my strftime( "%arg" ) index ###
  #
  #    abbr. year:        %y    18
  #    full year:         %Y    2018
  #    abbr. weekday:     %a    Wed
  #    full weekday:      %A    Wednesday
  #    abbr. month:       %b    Oct
  #    full month:        %B    October
  #    day of month:      %d    31
  #    date as mm/dd/yy:  %D    10/31/18
  #    locale date/time:  %c    Wed Oct 31 hh:mm:ss YYYY
  #    locale date:       %x    10/31/18
  #    locale time:       %X    12:20:48
  #    24-hr clock hour:  %H    HH
  #    12-hr clock hour:  %I    HH
  #    minutes:           %M    minutes
  #    seconds:           %S    seconds
  #    AM / PM:           %p    AM or PM
  #
  
  
# END main() ...


if __name__ == "__main__":
  main();
