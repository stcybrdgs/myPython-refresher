# virtualEvents.py
'''
this script set demonstrates how to bind to virtual events by
responding to user actions to cut, copy, or paste text in a
text entry widget

'''
# imports ======================================
from tkinter import *
from tkinter import ttk        

# functions ====================================

    
# tkinter ======================================    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

label = ttk.Label(root, text = 'Action Info: ')
label.pack()

# to bind to a virtual event, enclose the name of the event
# in double angle brackets <<name>>
entry.bind('<<Copy>>', lambda e: label.configure(text = 'Copy')) # CTRL + C
entry.bind('<<Paste>>', lambda e: label.configure(text = 'Paste')) # CTRL + V

# here, we create our own event binding using event_add() method
entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: label.configure(text = 'Odd Number'))

# use event_info() to view details about the virtual event
print(entry.event_info('<<OddNumber>>'))

# programatically trigger a virtual event
entry.event_generate('<<OddNumber>>')

'''
if you want to remove a virtual event:
entry.event_delete('<<OddNumber>>')
'''

# tk main loop =================================
root.mainloop()

# main ===============================
def main():
    print('Done.')

if __name__ == '__main__': main()    