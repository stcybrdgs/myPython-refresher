# Tk and Tkinter
# Tk is an open source toolkit used to build GUIs.
# It provides a library of GUI elements commonly used in desktop applications
# (ie, buttons, menus, windows, text fields).
# Tk was developed in early 90s as an extension for a scripting language called
# Tool Command Language (TCL)-- pronounced 'tickle.'
# It has since been ported to run on Windows, Mac OS, Unix, or Linux, so it
# is cross-platform compatible.
# When your python program makes a call to Tkinter, it will be accessing
# functions in the Tkinter package (which is written in Python), which parses your
# python script to look like Tk script and then passes them to the _tkinter extension
# module, which is written and compiled in C, and it is then able to make calls into
# the Widgets in the Tk library, which is implemented with C and Tcl.
# at the end of the chain, the Tk widgets use the Xlib library to draw GUI elements
# on the screen. The components will automatically assume the look and feel of the
# OS on which they are running.


# import all functions and vars from tkinter package
from tkinter import *

# use tk constructor to create a new top-level widget and assign it to var root
root = Tk()

# use the pack geometry management method to put a text label on the root widget
Label(root, text='Hello, Tkinter!').pack()

# run the main loop method for the root window
root.mainloop()