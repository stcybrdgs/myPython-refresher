# entryWidget.py
# when you need your user to enter a short text string, such as for
# a username or password, you should use the entry widget.
# it provides a simple, one-line text entry box for the user to type in the info,
# and it is limited to just one line.
# (so, )if you need the user to be able to enter multiple lines of text, then you will
# need to use the text widget instead.)

# imports ====================================
from tkinter import *
from tkinter import ttk

# globals ====================================
passState = 1

# functions ==================================
# display contents of entry field when entryInfoBttn is clicked
def getEntryInfo():
	if(entry.get() == ''):
		entryInfoLabel.config(text = 'EMPTY')
	else:
		entryInfoLabel.config(text = entry.get())

# clear the contents of the entry field when entryClearBttn is clicked
def clearEntryField():
	# rem to edit entry field you use insert() or delete()
	#     delete(startIndex, endIndex), where END includes final char
	entry.delete(0, END)
	getEntryInfo()

# insert a special message into entry field when showSpecialMessageBttn is clicked
def showSpecialMessage():
	clearEntryField()
	# insert(startIndex, textToEnter)
	entry.insert(0, 'This GUI was built with Tkinter!')
	entryInfoLabel.config(text = '')

# enable or disable the password entry field when togglePassStateBttn is clicked
def togglePassState():
	global passState
	if(passState == 1):
		passState = 0
		password.state(['disabled'])
	else:
		passState = 1
		password.state(['!disabled'])
	
# tkinter ====================================
root = Tk()

# entry fields
# rem width controls the initial character length of entry field
# rem entry does not have a set method, only a get method, so
#     to change contents of entry field, use insert and delete methods
entry = ttk.Entry(root, width = 30)
entry.pack()

password = ttk.Entry(root, width = 30)
password.pack()
password.insert(0, 'Enter your password')

# buttons
entryInfoBttn = ttk.Button(text = 'What\'s in the 1st entry field?')
entryInfoBttn.pack()
entryInfoBttn.config(command = getEntryInfo)

entryClearBttn = ttk.Button(text = 'Clear 1st Entry Field')
entryClearBttn.pack()
entryClearBttn.config(command = clearEntryField)

showSpecialMessageBttn = ttk.Button(text = 'Show Special Message')
showSpecialMessageBttn.pack()
showSpecialMessageBttn.config(command = showSpecialMessage)

togglePassStateBttn = ttk.Button(text = 'Toggle Password State')
togglePassStateBttn.pack()
togglePassStateBttn.config(command = togglePassState)

# labels
entryInfoLabel = ttk.Label(text = 'EMPTY')
entryInfoLabel.pack()

# main loop
root.mainloop()

# main =======================================
def main():
	# display 'Done' in console when tkinter app is closed
	print('Done')

if __name__ == '__main__': main()	