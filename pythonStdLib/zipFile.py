# python zipfile module

# the zipfile module lets you pick up some files and zip them together in a zip file
import zipfile

# open zip file and list contents
zip = zipfile.ZipFile('archive.zip', 'r')
print(zip.namelist())

# look at metadata in the zip folder
for meta in zip.infolist():
	print(meta)

info = zip.getinfo('purchases.txt')
print(info)

# access file in zip folder and print contents
print(zip.read('purchases.txt'))
with zip.open('books.txt') as f:
	print(f.read())

# extract a file from the zip file
zip.extract('purchases.txt')

# extract everything from the zip file
zip.extractall()

# close the zip file
zip.close()