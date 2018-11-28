# keyboardEvents.py
'''
while callbacks are only used with specific actions for various widgets such
as spinboxes, menuboxes, scrollbars, buttons, and so on, Tkinter can also
allow you to bind events to specific handlers so that you can respond to I/O
devices like the keyboard and the mouse. Such events include:
    
    ButtonPress    KeyPress
    ButtonRelease  KeyRelease
    Enter          Leave
    FocusIn        Motion
    FocusOut

'''
# imports ======================================
from tkinter import *
from tkinter import ttk        

# functions ====================================
def key_press(event):
    eventType = event.type
    eventWidget = event.widget
    eventChar = event.char
    eventKeySym = event.keysym
    eventKeyCode = event.keycode
    
    typeInfo.configure(text = eventType)
    widgetInfo.configure(text = eventWidget)
    charInfo.configure(text = eventChar)
    keySymInfo.configure(text = eventKeySym)
    keyCodeInfo.configure(text = eventKeyCode)

def shortcut(action):
    labelSpecial.configure(text = action)
        
# tkinter ======================================    
root = Tk()

# create label grid to report generic key press info
labelFrame = ttk.Frame(root)
labelFrame.grid(row = 0, column = 0, columnspan = 5)

typeLabel = ttk.Label(labelFrame, text = 'TYPE  ')
widgetLabel = ttk.Label(labelFrame, text = 'WIDGET  ')
charLabel = ttk.Label(labelFrame, text = 'CHAR  ')
keySymLabel = ttk.Label(labelFrame, text = 'KEYSYM  ')
keyCodeLabel = ttk.Label(labelFrame, text = 'KEYCODE  ')

typeLabel.grid(row = 0, column = 0)
widgetLabel.grid(row = 0, column = 1)
charLabel.grid(row = 0, column = 2)
keySymLabel.grid(row = 0, column = 3)
keyCodeLabel.grid(row = 0, column = 4)

typeInfo = ttk.Label(labelFrame, text = '      ')
widgetInfo = ttk.Label(labelFrame, text = '        ')
charInfo = ttk.Label(labelFrame, text = '      ')
keySymInfo = ttk.Label(labelFrame, text = '        ')
keyCodeInfo = ttk.Label(labelFrame, text = '         ')

typeInfo.grid(row = 1, column = 0)
widgetInfo.grid(row = 1, column = 1)
charInfo.grid(row = 1, column = 2)
keySymInfo.grid(row = 1, column = 3)
keyCodeInfo.grid(row = 1, column = 4)

# put a listenter on the keyboard for a generic key press
root.bind('<KeyPress>', key_press)

# create a label to display info for special key combinations
labelSpecial = ttk.Label(root, text = 'Special Keys:')
labelSpecial.grid(row = 2, column = 0, columnspan = 5)

# listen for special key combinations
root.bind('<Control-c>', lambda e: shortcut('Special Keys: Copy'))
root.bind('<Control-v>', lambda e: shortcut('Special Keys: Paste'))

'''
example keyboard event binding statements:

Event Format                    Event Description
------------------              -------------------
<Key>, <KeyPress>               User pressed any key
<KeyPress-Delete>               User pressed Delete key
<KeyRelease-Right>              User released Right Arrow key
a, b, c, 1, 2, 3, etc           User pressed a 'printable' key 
<space>, <less>                 ibid
<Shift_L>, <Control_R>          User pressed a 'special' key
<F5>, <Up>                      ibid
<Return>                        User pressed the Enter key
<Control-Alt-Next>              User pressed Ctrl+Alt+PageDown keys

'''
# tk main loop =================================
root.mainloop()

# main ===============================
def main():
    print('Done.')

if __name__ == '__main__': main()    