# createWidgets

# Widgets provide graphical components like menus, buttons, and text fields to allow
# the user to interact with the program that lies behind the widgets.
# Each widget is defined as a class within the Tkinter package.
# When you add a widget to your program with Tkinter, you are creating an
# instance of that class, ie a Python object.
#
# in Tk, all widgets in your program exist under a hierarchy, with a single root
# window at the very top. So, every time you create a new widget object in Tkinter,
# you will need to specify another widget as its parent in that hierarchy.


# import all functions and variables from the base Tkinter package
from tkinter import *

# import the themed Tk widgets
from tkinter import ttk

# instantiate the Tk class to create top-level parent widget for
# other widgets that you may create later. Each instance of the Tk() class
# will have its own associated Tcl interpreter
root = Tk()

# add a widget to the parent widget
# use ttk name as prefix to create a themed widget
# and pass root in as the parent widget
# and pass 0 or more parameters to configure the various properties of the widget
button = ttk.Button(root, text = 'Click Me')

# call pack method on button object to insert it into root window and display it
button.pack()

# to find out the current value of a property, use [] to index that property
# from the widget object
print(button['text'])

# one way to change the properties of the button:
button['text'] = 'Press Me'

# another way to change the properies is to use .config:
button.config(text = 'Push Me')

# rem when you assign properties to an object, they are stored to a dictionary
# within the object, and you can access that dictionary by using config()
# with keyword arguments that it uses to pass the new value into the dictionary
# you can also use config method to see all properties for a widget object by
# calling it with no parameters (this returns the entire dict of tuples):
print(button.config())

# rem every Tkinter object has a unique name that is used by Tcl to reference
# that specific widget when interfacing with Tk-- this name is different than
# the name of the python variable that is being used to reference the object.
# here, we are using 'button' as the python var, but to see the underlying Tk
# name (which is a random unique identifier), we can use the Str function on
# the button:
print('The Tk button name is: ', str(button))

# the root widget will be given the special name of '..
print('The Tk root name is: ', str(root))

# run the main loop method for the root window
root.mainloop()
