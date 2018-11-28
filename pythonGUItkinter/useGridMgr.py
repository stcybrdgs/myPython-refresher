# useGridMgr.py

# imports ======================================
from tkinter import *
from tkinter import ttk        

# tkinter ======================================    
root = Tk()

# make a bunch of labels for the root window
# rem by default, widgets are placed in the center of the grid space
#     that is allocated for them
# rem use the sticky property to control which side of the cell
#     your widget anchors to
# rem The weight property tells the row or column how much it should
#     grow relative to the other rows or columns to fill the space
#     created when the parent widget is resized. By default all rows and
#     columns have a weight of zero, meaning that they will not resize
#     to fill the parent. We can configure weights by calling the
#     row configure and column configure on the parent widget.
colors = {'red', 'orange', 'yellow', 'green', 'blue', 'purple'}
r = 0
c = 0
i = 0
for color in colors:
    if( i == 2 ):
        i = 0
        c = 0
        r += 1
    if( c == 0 ): s = 'w'
    else: s = 'e'
    ttk.Label(root,
              text = color,
              background = color
             ).grid(
        row = r,
        column = c,
        sticky = s
        )
    i += 1
    c += 1




# tk main loop =================================
root.mainloop()

# main ===============================
def main():
    print('Done.')


if __name__ == '__main__': main()    