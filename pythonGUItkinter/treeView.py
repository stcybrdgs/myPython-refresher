# treeView.py
# the treevew widget can be used to display a list of items that the user
# can interact with and make selections from.
# the view can be presented on a single level or as part of a
# multi-tiered hierarchy.

# imports ====================================
from tkinter import *
from tkinter import ttk

# tkinter ====================================
root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()

# to use the treeview, you need to insert items, each of which
# act as a node on the tree and are accessed by unique IDs.
# you can choose the names when you create the nodes, or you can
# let TKinter automatically generate a unique ID for each node
# if nothing has been inserted to the tree, then it automatically
# creates a root node with the special ID of empty string
# here, we'll create a node that uses empty string, and then
# for the index, we will identify the position in the list under
# the parent node to insert the new item.
# the fourth+ parameters (ie, **kv) are optional, and you can add as many as you need to
treeview.insert('', '0', 'item1', text = 'First Item') # (parent, index, iid=None, **kv)
treeview.insert('', '2', 'item2', text = 'Second Item')
# you may include tags property among your **kv
treeview.insert('', 'end', 'item3', text = 'Third Item', tags=('software')) 
treeview.insert('', 'end', 'item4', text = 'Fourth Item')
treeview.insert('', 'end', 'item5', text = 'Fifth Item')

# add images, using the subsample() method to shrink it
logo = PhotoImage (file = 'python_logo.gif').subsample(10,10)
treeview.insert('item2', 'end', 'pythonLogo', text='Python', image = logo)

# change the height property to indicate how many items you want treeveiw
# to be able to display at one time
treeview.config(height = 10)

# you can rearrange items in the treeview with the move() method, but you
# can't move an item to be underneath one of its own
treeview.move('item2', 'item1', 'end')

# By default, items in the tree view are created in the closed position.
# We can change this by modifying the open property with the item method.
treeview.item('item1', open = 'True')
treeview.item('item2', open = 'True')

# you can check on the open/close status
# where result returns a boolean 1 = T, 0 = F
# like this:
openStatus = treeview.item('item1', 'open')

# let label show open status of item1:
label = ttk.Label(root, text = 'statusInfo')
label.pack()
label.config(text = str(openStatus))

# remove item from treeview using detach()
# even though you detach an item, it still exists, so you can
# still manipulate it as needed
# detach the item (it will disappear from the treeview)
treeview.detach('item3')

# use move() to reattach item3 under item2 at the top of
# the item2 listing
treeview.move('item3', 'item2', '0') # pathname move item parent index
treeview.move('item1', 'item5', '0')

# to completely remove an item, use delete()
treeview.delete('item4')

# insert a new top level index
treeview.insert('', '0', 'item0', text = '0th Item')


# add an additional column to the tree and name it version
treeview.config(columns = ('version'))
treeview.column('version',
				width = 100,
				anchor = 'center'
				) # column(nameOfColumn, **args)

# rever to the main treeview column as #0
treeview.column('#0', width = 150)

# use heading method to display column names
treeview.heading('version', text = 'Version')
treeview.heading('#0', text = 'Main')

# to configure a value for a slot within a column, use set()
# .set(itemInHierarchy, columnForContent, content)
treeview.set('item0', 'version', '0')
treeview.set('pythonLogo', 'version', '3.4.1') 

# as with text, you can add tags in your treeview
# by adding tags to treeview items, you can modify their
# properties as groups
# tags may be added at the time of creation with the tags property
# or they may be added later using the "item" method
treeview.item('pythonLogo', tags=('software'))
treeview.tag_configure('software', background = 'yellow')

# treeview callback event -----------------------
#
# the treeview widget does not support a command callback to
# execute code when an item is selected; instead, you can listen to
# virtual events from the treeview (there's three of these events)
# one such event is the 'bind' method which does a callback when
# a selection is made
treeviewSelectLabel = ttk.Label(root, text = 'Treeview Selection')
treeviewSelectLabel.pack()

def callback(event):
	string = 'Treeview Selection ' + str(treeview.selection())
	treeviewSelectLabel.configure(text = string)

# use 'bind' to configure the callback event
treeview.bind('<<TreeviewSelect>>', callback)

# notice that by default the treeview uses an 'extended select mode'
# that allows multiple items to be selected at once;
# you may modify the select mode by setting the 'select mode' property
# (if you want the user to only be able to select one item at a
# time, specify 'browse' mode)
treeview.config(selectmode = 'browse') # select one item at a time
treeview.config(selectmode = 'none') # select no item

# to programmatically select tree items, use
# selection_add
treeview.selection_add('pythonLogo')

# rem lu selection_move and selection_toggle

# to programmatically unselect items, use selection_remove
treeview.selection_remove('pythonLogo')

# to programmatically toggle items, use selection_toggle,
# and the item will be either selected or unselected based on
# the current selected state of the item
treeview.selection_toggle('pythonLogo')

# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()