# cascadingMenus.py

# imports ====================================
from tkinter import *
from tkinter import ttk
# menus are not part of ttk

# tkinter ====================================
root = Tk()
root.title('My New App')
root.geometry('240x140')
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
# (event binding can be used to actually create the shortcuts)
file_.entryconfig('New', accelerator = 'Ctrl + N')
file_.entryconfig('Save', accelerator = 'Ctrl + S')

# you can use PhotoImage and .entryconfig to add images to your menu
logo = PhotoImage(file = 'python_logo.gif').subsample(15,15)
file_.entryconfig('Open...', image = logo, compound = 'left')

# you can disable menu items using state
file_.entryconfig('Delete', state = 'disabled')

# in addition to adding commands to a menu, you can also add other menus to create submenus
# here, we can create a save submenu
file_.delete('Save') # delete original save menu item
save = Menu(file_) # create save menu item as child of the file_ menu item
file_.add_cascade(menu = save, label = 'Save')
save.add_command(label = 'Save As...', command = lambda: menuInfo.configure(text = 'Saving As...'))
save.add_command(label = 'Save All...', command = lambda: menuInfo.configure(text = 'Saving All...'))
save.entryconfig('Save As...', accelerator = 'Ctrl + S') # cormat shortcut keys

# you can also add radio buttons and check buttons to menus
choice = IntVar()
edit.add_separator()
choose = Menu(edit)
edit.add_cascade(menu = choose, label = 'Select Level   ')
choose.add_radiobutton(label = 'One', variable = choice, value = 1,
					   command = lambda: menuInfo.configure(text = 'Select Level One'))
choose.add_radiobutton(label = 'Two', variable = choice, value = 2,
					   command = lambda: menuInfo.configure(text = 'Select Level Two'))
choose.add_radiobutton(label = 'Three', variable = choice, value = 3,
					   command = lambda: menuInfo.configure(text = 'Select Level Three'))

# you can create popup menus at specific locations on the screen with post() method
# this method takes (x,y) coordinates of the location for the popup menu
# based on the entire screen (not just the Tk window ), starting from top left hand corner
file_.post(400,300)

# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()