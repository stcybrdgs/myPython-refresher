# cascadingMenus.py


# imports ====================================
from tkinter import *
from tkinter import ttk
# menus are not part of ttk

# tkinter ====================================
root = Tk()
root.geometry('200x100')
# tell Tk object that each meunu in interface should not be
# of the tearoff type (Tkinter defaults to tearoff menus as a
# legacy feature, but tearoff menus oare not part of modern GUI design)
root.option_add('*tearOff', False)

# create a menu bar object and assign it to the root window
menubar = Menu(root)

# configure the root window to use the menu bar object as the menu
root.config(menu = menubar)

# rem now each menu item that you create will be a new menu object
# which is a child of the menu bar object

# create menu items
file_ = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
about = Menu(menubar)

# add menu items to the menu bar
menubar.add_cascade(menu = file_, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')
menubar.add_cascade(menu = about, label = 'About')

# put an info label on root window
menuInfo = ttk.Label(root, text ='menuInfo')
menuInfo.pack()


# add some commands to the file menu
# File commands
file_.add_command(label = 'New', command = lambda: menuInfo.configure(text='New File'))
file_.add_command(label = 'Save', command = lambda: menuInfo.configure(text='Save File'))
file_.add_command(label = 'Delete', command = lambda: menuInfo.configure(text='Delete File'))

# Edit commands
edit.add_command(label = 'Erase', command = lambda: menuInfo.configure(text='Erase File'))
edit.add_command(label = 'Append', command = lambda: menuInfo.configure(text='Append to File'))

# add separator line between menu elements
file_.add_separator()
file_.add_command(label = 'Open...', command = lambda: menuInfo.configure(text='Open File'))
file_.add_command(label = 'Close', command = lambda: menuInfo.configure(text='Close File'))

# add shortcut properties using the accelerator property of the entry config method
# rem the accelerator property does not actually create the shortcut but only
# formats the shortcut key to the right of the menu item
file_.entryconfig('New', accelerator = 'Ctrl + N')
file_.entryconfig('Save', accelerator = 'Ctrl + S')

# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()