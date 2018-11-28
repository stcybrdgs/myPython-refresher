# usePlaceMgr.py
'''
when your application requires exact control of where a widget
is placed, then you should turn to the place manager. With the
place geometry manager, you can specify the location and size of
a widget in absolute and/or relative terms as they relate to the
parent window. You can create very detailed layouts and stack widgets
on top of each other in ways that would not be possible with the other
geometry managers. The downside to using the place manager is that it
can become difficult to ensure that multiple widgets maintain the proper
size and location relative to each other if the parent window or frame
is resized. For these reasons, you might consider using the place
manager when you need to craft a very specialized piece of the GUI,
and to do that inside of a frame which you prevent from changing in size
if the rest of the GUI is resized. 
'''

# imports ======================================
from tkinter import *
from tkinter import ttk        

# tkinter ======================================    
root = Tk()

root.geometry('640x480+600+200')

# tk main loop =================================
root.mainloop()

# main ===============================
def main():
    print('Done.')


if __name__ == '__main__': main()    