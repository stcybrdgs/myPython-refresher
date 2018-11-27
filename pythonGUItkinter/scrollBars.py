# scrollBars.py
#
# if you GUI includes widgets that are too large to view in the
# available space, then you can include a scroll bar to enable the user
# to selectively view different sections of it.
# in Tk, scrollbars are their own unique widgets, rather than just
# being a sub feature of other widgets

# imports ====================================
from tkinter import *
from tkinter import ttk

# tkinter ====================================
root = Tk()
text = Text(root, width = 40, height = 10, wrap = 'word')
text.grid(row = 0, column = 0)

# use yview for a vertical scroll bar
# yview tells the text widget how far the scrollbar has been moved
ybar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview)
ybar.grid(row = 0, column = 1, sticky = 'ns') # ns = north/south
# tell text widget to communicate with scroll bar
text.config(yscrollcommand = ybar.set)

# you can use scrollbars with many different types of widgets, including:
# X-Scroll          Y-Scroll
# ---------------------------
# text               text
# canvas             canvas
# treeview           treeview
# entry
# spinbox
# combobox

# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()