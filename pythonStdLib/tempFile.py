# python Tempfile module

# import tempfile module
# rem use this module to create temporary files in python
import tempfile

# create a temporary file
tempFile = tempfile.TemporaryFile()

# write a number to the temp file
# rem use b prefix to change string into a byte literal
tempFile.write(b'012345')
tempFile.seek(0)

# read from the temp file
print(tempFile.read())

# close the temp file
tempFile.close()