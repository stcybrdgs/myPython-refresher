#!/usr/bin/python3
# helloTkinter2

# This is my modified exercise file from
# Python GUI Development with Tkinter with Baron Stone

# imports() ========================================= 
from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)
        
        ttk.Button(master, text = 'Stacy',
                   command = self.stacy_hello).grid(row = 2, columnspan = 2)
        
    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')

    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')
    
    def stacy_hello(self):
        self.label.config(text = 'Hi, Stacy')
        


# main() =========================================            
def main():            
    # create master Tk widget
    root = Tk() 
    
    # instntiate HelloApp obj, name it app, and pass root obj to Tk widget
    # to serve as master widget
    app = HelloApp(root)
    
    # enter the listening loop
    root.mainloop()
    
if __name__ == "__main__": main()
