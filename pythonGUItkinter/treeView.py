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
treeview.insert('', 'end', 'item3', text = 'Third Item')
treeview.insert('', 'end', 'item4', text = 'Fourth Item')

# add images, using the subsample() method to shrink it
logo = PhotoImage (file = 'python_logo.gif').subsample(10,10)
treeview.insert('item2', 'end', 'pythonLogo', text='Python', image = logo)

# change the height property to indicate how many items you want treeveiw
# to be able to display at one time
treeview.config(height = 5)

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
treeview.move('item3', 'item2', '0')

# to completely remove an item, use delete()
treeview.delete('item4')

# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()