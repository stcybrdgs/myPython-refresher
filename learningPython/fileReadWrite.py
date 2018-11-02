#
# Read and write files using the built-in Python file methods
#

# note: Python already knows about files-- there's 
# no need to import anything in order to work with them
import calendar

def main():  
  # Open a file for writing and create it if it doesn't exist
  # syntax is open ( "fileToOperateOn", "kindOfAccessYouWant" )
  # open( file, mode, buffering, encoding, errors, newline, closefd, opener )
  # here, w means write access and + means create file if does not exist
  f = open( "textfile.txt", "w+" )  

  # write some lines of data to the file
  for i in range(10):
    f.write( "This is line " + str(i) + "\r\n" )
  
  # close the file when done
  f.close()
  
  # write days of week to text file
  f = open( "textFile2.txt", "w+" )
  
  for day in calendar.day_name:
    f.write( str(day) + "\r\n" )
  
  f.close()
  f = open( "textFile2.txt", "a" )
  f.write( "Have a good week!" )
  f.close()

  # Open the file back up and read the contents
  f = open( "textFile2.txt", "r" )
  
  # only read the file if it successfully opened
  if f.mode == 'r': 
    contents = f.read()
    print( contents )     
  
  f.close()

  # Open the file and read lines
  f = open( "textFile2.txt", "r" )

  if f.mode == 'r': 
    fl = f.readlines()
    for x in fl:
      print( contents )   
  
  f.close()

if __name__ == "__main__":
  main()
