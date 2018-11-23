# textWidget.py
# rem read through tk documentation for all of the great things you can do
#     with the text widget

# imports ====================================
from tkinter import *
from tkinter import ttk
# the text widget is not a themed widget, btw

# global =====================================
disabled = 0

# functions ==================================
def getAllText():
	# get all text that is in the text box
	textInfo = text.get('1.0', 'end')
	label.config(text = textInfo)
	
def getLine1():
	# get text from start of text box to end of first logical line
	# ie, up until the first invisible end of line character
	textInfo = text.get('1.0', '1.end')
	label.config(text = textInfo)

def insertPass():
	# get password
	passInfo = password.get()
	
	# insert password two logical lines below start of textbox
	text.insert('1.0 + 2 lines', '\n' + passInfo)

def replaceLine1():
	#text.delete('1.0', '1.0 lineend')
	text.replace('1.0', '1.0 lineend', 'The first line has been replaced')
	
def clearText():
	# delete method
	# if you provide one parameter, the method will delete the character at the
	# specified position, ie text.delete('1.0'),
	# but if you provide 2 parameters, it will delete the range from the first parameter
	# to the last parameter, non-inclusive
	text.delete('1.0', 'end')

def disableText():
	global disabled
	if (disabled == 0):
		disabled = 1
		text.config(state = 'disabled')
		buttonDisable.config(text = 'Enable Text Field')
	else:
		disabled = 0
		text.config(state = 'normal')
		buttonDisable.config(text = 'Disable Text field')

# tkinter ====================================
root = Tk()

# make a text box
text = Text(root, width = 40, height = 10)
text.pack()

# control where the text box will wrap
# rem the wrap attribute can be 'char', 'none', or 'word'
text.config(wrap='word', relief = RIDGE) 

# the text widget needs to index characters across multiple lines,
# so it accepts indices arguments of specially formatted strings
# ' base modifer modifier', where base is starting point and
# the modifiers are optional to adjust the index from the starting point,
# a common type of base format is line.char, where,
# for example 4.2 would refer to th eposition in front of char 2 on line 4;
# base 1.0 would refer to the beginning of the text box.
# 'end' refers to the last position in the text box
# you can also increment +/- by # chars or # lines
# or you can use linsestart, lineend, wordstart, and wordend
# to move the pointer  as needed
# AND you can string together as many of these modifiers as you need to, and
# they will be evaluated in order from the left to the right.

# entry field for password
password = ttk.Entry(root, width = 30)
password.pack()

# button to return the entire contents of the text widget
buttonAll = ttk.Button(root, text = 'Get All Text')
buttonAll.pack()
buttonAll.config(command = getAllText)

# button to return just the first logical line
buttonLine1 = ttk.Button(root, text = 'Get 1st Line of Text')
buttonLine1.pack()
buttonLine1.config(command = getLine1)

# button to insert password into text field
buttonInsertPass = ttk.Button(root, text = 'Insert Password')
buttonInsertPass.pack()
buttonInsertPass.config(command = insertPass)

# button to replace the first line in the text field
buttonReplace = ttk.Button(root, text = 'Replace First Line')
buttonReplace.pack()
buttonReplace.config(command = replaceLine1)

# button to clear the text field
buttonClear = ttk.Button(root, text = 'Clear Text')
buttonClear.pack()
buttonClear.config(command = clearText)

# button to enable/disable text field
buttonDisable = ttk.Button(root, text='Disable Text Field')
buttonDisable.pack()
buttonDisable.config(command = disableText)

# label to display text returned from each button
label = ttk.Label(root, text = 'empty')
label.pack()

# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()