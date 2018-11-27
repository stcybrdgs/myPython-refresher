# useGridMgr.py

# imports ======================================
from tkinter import *
from tkinter import ttk        

# tkinter ======================================    
root = Tk()

# make a bunch of labels for the root window
# rem by default, widgets are placed in the center of the grid space
#     that is allocated for them
colors = {'red', 'orange', 'yellow', 'green', 'blue', 'purple'}
r = 0
c = 0
i = 0
for color in colors:
    if( i == 2 ):
        i = 0
        c = 0
        r += 1
    ttk.Label(root,
              text = color,
              background = color
             ).grid(
        row = r,
        column = c
        )
    i += 1
    c += 1

# tk main loop =================================
root.mainloop()

# main ===============================
def main():
    print('Done.')


if __name__ == '__main__': main()    