# comboAndSpinBoxes.py

# combo and spin boxes can be used to present the user with choices
# in a manner that is more compact than what might be provided with
# a bunch of radio and check boxes.
# rem the combo box is a drop menu
# rem the spin box is a rotating menu that shows one option at a time

# imports =============================
from tkinter import *
from tkinter import ttk

# functions ===========================
def getMonth():
	thisMonth = 'Month is ' + str(month.get())
	labelGetMonth.config(text = thisMonth)

# tkinter =============================
root = Tk()

# combobox for month
monthLabel = ttk.Label(root, text = 'Select Month:')
monthLabel.pack()
month = StringVar() # holde a selected value in combo box
month.set('Jan') # initial value
combobox = ttk.Combobox(root, textvariable = month) # textvariable is selected value
combobox.pack()
combobox.config(
	values = (
		'Jan','Feb', 'Mar', 'Apr', 'May', 'Jun',
		'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
		)
	)

# use button to get month and show it in label
monthStr = 'Month is ' + month.get()
labelGetMonth = ttk.Label(root, text = monthStr)
bttnGetMonth = ttk.Button(root, text = 'Get Month')
bttnGetMonth.config(command = getMonth)
labelGetMonth.pack()
bttnGetMonth.pack()

# spinbox
# the spinbox is not available as a ttk widget, only as an original tk widget
# so to create it, you don't need the ttk prefix
# the from parameter uses an uderscore to differentiate it from the python keyword
year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()





# main loop
root.mainloop()


# main =======================================
def main():
	# display 'Done' in console when tkinter app is closed
	print('Done')

if __name__ == '__main__': main()