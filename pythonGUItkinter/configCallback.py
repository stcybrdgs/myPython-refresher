# configCallback.py

# imports ======================================
from tkinter import *
from tkinter import ttk        

# globals ======================================
labelString = ''

# tkinter ======================================    
root = Tk()


def callback(arg):
    global labelString
    labelString = labelString + str(arg)
    label.config(text = labelString)

# to pass an argument to the callback function, use lambda to
# create an anonymous function, otherwise commmand will return the result of
# the function (including None) rather than simply calling the function
ttk.Button(root, text = 'Click Me!', command = lambda: callback('|')).pack()
label = ttk.Label(root, text = 'Callback Info')
label.pack()

# tk main loop =================================
root.mainloop()

# main ===============================
def main():
    print('Done.')


if __name__ == '__main__': main()    