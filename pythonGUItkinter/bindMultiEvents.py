# bindMultiEvents.py
'''
this script set demos
how to bind single widgets to multiple events and
how to bind single events to multiple widgets
'''
# imports ======================================
from tkinter import *
from tkinter import ttk        

# functions ====================================
def allLabels(e):
    labelOne.configure(text = 'Escape')
    labelTwo.configure(text = 'Escape')
    labelThree.configure(text = 'Escape')
    
# tkinter ======================================    
root = Tk()

labelOne = ttk.Label(root, text = 'Label One')
labelOne.pack()

labelTwo = ttk.Label(root, text = 'Label Two')
labelTwo.pack()

labelThree = ttk.Label(root, text = 'Root')
labelThree.pack()

# add event binding to labelOne
labelOne.bind('<ButtonPress>',
              lambda e: labelOne.configure(text = 'Generic Button Press'))
labelOne.bind('<1>',
              lambda e: labelOne.configure(text = 'Mouse Button 1'))

# add event to both labels by binding it to the root window
root.bind('<1>',
          lambda e: labelThree.configure(text = 'Mouse Left Click'))
root.bind('<2>',
          lambda e: labelThree.configure(text = 'Mouse Scroll Button'))
root.bind('<3>',
          lambda e: labelThree.configure(text = 'Mouse Right Click'))
root.bind('<Motion>',
          lambda e: labelThree.configure(text = 'Mouse Moved'))

# remove a binding
root.unbind('<Motion>')

# apply an event binding to multiple windows / widgets
# so that event is triggered no matter which window is in scope
root.bind_all('<Escape>', allLabels)

# tk main loop =================================
root.mainloop()

# main ===============================
def main():
    print('Done.')

if __name__ == '__main__': main()   