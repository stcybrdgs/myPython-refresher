# tkinter
# displaying text and images with labels

# imports =========================
from tkinter import *
from tkinter import ttk

# parent object
root = Tk()

# first label
label = ttk.Label(root, text = 'Hello, Tkinter')
label.pack()

# second label with style configurations
label2 = ttk.Label(root, text = 'I am really enjoying reading the Jim Butcher series about Harry Dreseden')
label2.config(
	wraplength = 150,
	justify = CENTER,
	foreground = 'white',
	background = 'blue',
	font = ('Courier', 14, 'bold')
)
label2.pack()


# add an image to your label
# the PhotoImage class is used to display color images within Tkinter
# and it can use GIF, PGM, or PPM files,
# if you want to use a different file type, then you'll need an external library
# to convert it to GIF, PGM, or PPM (ie, you could use the PYthon Image Library)
logo = PhotoImage(file = 'python_logo.gif')
label3 = ttk.Label(root, image = logo)
label3.config(text = 'Python')
label3.config(compound = 'text')
label3.config(compound = 'center')
label3.config(
	foreground = 'orange',
	font = ('Arial Bold', 24)
)
label3.pack()

# rem for your images to display, they must remain in scope, so if you store your image
# in a variable that is local to a function, then when the function completes, the image
# will be garbage collected and the image will disappear from your GUI;
# the same issue applies to scenarios where your PhotoImage object is created in a class
# object per the constructor method. . . when the object loses scope, the image will
# be garbage collected and Tkinter won't display it anymore.
# So, make sure your images are stored in such a way that they won't be garbage collected
# for as long as you need the image to remain active in the widget.
# a good way to handle this issue is to store your logo within a label as we did above

root.mainloop()
