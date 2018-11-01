#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil # shell utilities
from shutil import make_archive

def main():
  # make sure textfile.txt exists in the directory
  if path.exists( "textfile.txt" ):

      # get the path to the file
      src = path.realpath( "textfile.txt" )
      print( "src: " + str( src ) )

      # get the directory and the filename
      root_dir, file_name = path.split( src )
      print( "root_dir: " + str( root_dir ) )
      print( "file_name: " + str( file_name ) )  
     
      # make a duplicate of the file and call it v2
      # (file will have new meta data re permissions, mod time, etc)
      dst = str(file_name).replace( ".", "_v2." )
      shutil.copy( src, dst )      # copy the src file

      # make another dupe, this time v3, but with original meta data
      dst = str(file_name).replace( ".", "_v3." )
      shutil.copy( src, dst )      # copy the src file
      shutil.copystat( src, dst )  # copy the src-file meta data

      # make a duplicate of the original file and append "bak" to the name (for "backup")
      dst = str( file_name ) + ".bak"
      shutil.copy( src, dst )  

      # rename v3 to v4
      os.rename( "textfile_v3.txt", "textfile_v4.txt" )
    
      # now put things into a ZIP archive
      shutil.make_archive( "archive", "zip", root_dir )  # (basename, format, directory)

    
if __name__ == "__main__":
  main()
