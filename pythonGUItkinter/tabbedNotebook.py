# tabbedNotebook.py
# A common mechanism for organizing multiple displays in modern GUIs is the use of tabs.
# In TK, the notebook widget can be used for that type of navigation.
# You can add multiple frames as the pages of a notebook and then switch between
# which of those pages is displayed by selecting from the corresponding tabs.

# imports ====================================
from tkinter import *
from tkinter import ttk

# functions ==================================
# display the index of the currently selected tab
def showCurrentTab():
	rootLabel.config(text = notebook.index(notebook.select()))
	
# tkinter ====================================
root = Tk()

# create a tabbed notebook
notebook = ttk.Notebook(root)
notebook.pack()

# add tabs to the notebook
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
notebook.add(frame1, text = 'One', padding = (20, 20))
notebook.add(frame2, text = 'Two')
notebook.add(frame3, text = 'Three')
notebook.insert(2, frame4, text = 'Four') # insert to the right of tab 2

# create a button on tab one
ttk.Button(frame1, text = 'Click Me').pack()

# use root-level button and label to display the index of the currently selected tab
rootButton = ttk.Button(root, text = 'Show Current Tab')
rootLabel = ttk.Label(root, text = 'Current Tab', padding = (10, 10))
rootLabel.pack()
rootButton.pack()
rootButton.config(command = showCurrentTab)

# modify tabs
notebook.tab(1, state = 'disabled') # disable a tab
notebook.tab(2, state = 'hidden') # hide a tab
notebook.tab(2, state = 'normal') # restore a tab

# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()