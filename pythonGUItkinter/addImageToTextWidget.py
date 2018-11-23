# addImageToTextWidget.py
# add a photo image to text widget the same way you add to entry widget

# imports ====================================
from tkinter import *
from tkinter import ttk
# the text widget is not a themed widget, btw


# tkinter ====================================
root = Tk()

# create text field
text = Text(root,
			width = 40,
			height = 10,
			relief = SOLID,
			wrap = 'word'
			)
text.pack()

# insert text
text.insert('1.0', 'This is the default text.')

# insert image
pyImage = PhotoImage(file='python_logo.gif')
smallPyImage = pyImage.subsample(5,5) 
text.image_create('insert', image = smallPyImage)


# insert button
button = Button(text, text = 'Click Me')
text.window_create('insert', window = button)


# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()