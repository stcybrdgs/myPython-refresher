# 
# Example file for retrieving data from the internet
#

# import urllib, which contains the classes and code 
# that you need to make http requests
import urllib.request

def main():
  # connect to the google website
  webUrl = urllib.request.urlopen( "http://www.google.com" )
  
  # rem: returned code of 200 means connected with no errors
  print( "result code: " + str( webUrl.getcode() ) )

  # read some data and print it out
  data = webUrl.read()
  print( data )

  # copy page source to a txt file
  f = open( "googlePage.txt", "w+" )
  f.write( str( data ) )
  f.close()

if __name__ == "__main__":
  main()
