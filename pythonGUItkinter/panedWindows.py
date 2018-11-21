# panedWindows.py
#
# the paned window is a widget that can be used to split up sections of the user interface.
# it is a geometry-management widget that can hold other widgets by stacking them
# vertically or horizontally. Users can click and drag to adjust the relative size of the widgets.
# any type of widget can be added to the pane window, but it is commonly used to hold frames

# imports ====================================
from tkinter import *
from tkinter import ttk

# tkinter ====================================
root = Tk()
panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL) # orient can be horizontal or vertical
panedwindow.pack(fill = BOTH, expand = 'True')

frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)

# the add() method will line frames out horizontally or vertically, depending upon how you
# selected orient in the original Panedwindow() call
panedwindow.add(frame1, weight = 1)
panedwindow.add(frame2, weight = 4)

# use insert() instead of add() to place frame in between existing frames
# by default, the frame will have a weight of 0 if not explicitly specified
# but the user can resize it manually within the app window
panedwindow.insert(1, frame3) # insert (index, frame)

# tkinter loop
root.mainloop()


# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()