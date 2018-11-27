# usePackMgr.py

# imports ======================================
from tkinter import *
from tkinter import ttk        

# tkinter ======================================    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(fill = BOTH,     # fill in x & y
                                      expand = True)   # expand in x & y on resize
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(fill = BOTH,       # fill in x & y
                                      expand = False)  # no expand on resize
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(fill = BOTH,      # fill in x & y
                                      expand = True)   # expand in x & y on resize
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'red').pack(side = LEFT,
                                   ipadx = 10,
                                   ipady = 10)         # inner padding
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'brown').pack(side = BOTTOM,
                                     anchor = 'se',
                                     padx = 10,
                                     pady = 10)        # outer padding
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'orange').pack(side = RIGHT)

# use pack_slaves() to return list of all widgets being
# managed by the pack manager
for widget in root.pack_slaves():
    print(widget)

# use pack_slaves with loop to set packing properties for all widgets
for widget in root.pack_slaves():
    widget.pack_configure(fill = BOTH, expand = True)
    
# find out what the current value of the packing properties are
# for a specific widget
print('\nUsing pack_info() to get current values of packing properties. . . ')
i = 0
for widget in root.pack_slaves():
    info = widget.pack_info()
    print('widget ', i, ': \n', info)
    i += 1

# tk main loop =================================
root.mainloop()

# main ===============================
def main():
    print('Done.')


if __name__ == '__main__': main()    