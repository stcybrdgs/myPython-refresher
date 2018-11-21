#!/usr/bin/python3
# checkAndRadioBttns.py
#
# this file contains practice for check buttons and radio buttons
# check buttons (for selecting 1 of 2 choices) and
# radio buttons (for selecting 1 of many choices)
# are great for letting a user select or unselect options from a set of choices
# and the buttons can also store a binary value (1 when selected, 0 when not selected)
#
# the 4 variable classes that are available in Tkinter are:
#     BooleanVar
#     DoubleVar
#     IntVar
#     StringVar


# imports ========================
from tkinter import *
from tkinter import ttk


# functions ======================
def checkSelect():
	spamLabel.config(text = spam.get())

def displayBreakfast():
	breakfastLabel.config(text = breakfast.get())
		
# tkinter ========================
root = Tk()


# buttons ------------------------
# check button
checkbutton = ttk.Checkbutton(root, text = 'SPAM')
checkbutton.pack()

spam = StringVar()
spam.set('SPAM!')
checkbutton.config(
	variable = spam,
	onvalue = 'SPAM, Please!',
	offvalue = 'Boo, SPAM!'
	)

# radio button
# each radio button is its own object, and they're all tied together by a common variable
breakfast = StringVar()
breakfast.set('Toast')
ttk.Radiobutton(root, text = 'Spam', variable = breakfast, value = 'Spam').pack()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast, value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast, value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'Toast', variable = breakfast, value = 'Toast').pack()

# button button
button = ttk.Button(root, text = 'What\'s for Breakfast?')
button.pack()
					

# labels --------------------------
spamLabel = ttk.Label(root, text = spam.get())
spamLabel.pack()

breakfastLabel = ttk.Label(root, text = breakfast.get())
breakfastLabel.pack()


# events --------------------------
checkbutton.config(command = checkSelect)
button.config(command = displayBreakfast)


# tk main loop
root.mainloop()


# main() =========================================            
def main():
	print('done.')


if __name__ == '__main__': main()