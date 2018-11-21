# comboAndSpinBoxes.py

# combo and spin boxes can be used to present the user with choices
# in a manner that is more compact than what might be provided with
# a bunch of radio and check boxes.
# rem the combo box is a drop menu
# rem the spin box is a rotating menu that shows one option at a time

# imports =============================
from tkinter import *
from tkinter import ttk

# tkinter =============================
root = Tk()

# combo box
month = StringVar() # use var to hold value for combo box

# rem textvariable is the variable that will be tied to the
# value that is selected in the combo box
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(
	values = (
		'Jan','Feb', 'Mar', 'Apr', 'May', 'Jun',
		'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
		)
	)
month.set('Jan')



# main loop
root.mainloop()


# main =======================================
def main():
	# display 'Done' in console when tkinter app is closed
	print('Done')

if __name__ == '__main__': main()