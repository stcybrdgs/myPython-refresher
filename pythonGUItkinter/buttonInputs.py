# buttonInputs.py
# tkinter
# this file contains practice scripts for button-triggered events


# imports ========================
from tkinter import *
from tkinter import ttk

# global =========================
clickCount = 0


# functions ======================
def callback():
	global clickCount
	clickCount += 1
	if (clickCount == 3):
		s = 'Hat Click!'
	elif (clickCount == 5):
		s = 'Too many clicks!'
		clickCount = 0
		button.state(['disabled'])  # disable the button after 5 clicks
		label.config(text = 'Click Me Disabled')
	else:
		s = 'Clicked'
	label2 = ttk.Label(root, text = s)
	label2.pack()

def resetCallback():
	global clickCount
	clickCount = 0
	button.state(['!disabled'])  # enable the button
	label.config(text = 'Click Me Enabled')

		
# tkinter ========================
root = Tk()

# buttons
button = ttk.Button(root, text = 'Click Me')
button.pack()

logo = PhotoImage (file = 'python_logo.gif')
small_logo = logo.subsample(5,5)  # take every 5th pixel in X direction and Y direction
resetButton = ttk.Button(root, text = 'RESET')
resetButton.config(image = small_logo, compound = CENTER)
resetButton.pack()

# labels
label = ttk.Label(root, text = 'Click Me Enabled')
label.config(font = ('Courier', 12, 'underline'))
label.pack()

# events
button.config(command = callback)
resetButton.config(command = resetCallback)

# tk main loop
root.mainloop()


# main() =========================================            
def main():
	print('done.')


if __name__ == '__main__': main()