# mouseEvents.py
'''
this script set creates a simple drawing program to demonstrate
how to bind mouse events to a widget, in this case a canvas widget

rem mouse is mapped as follows:
1 - left button
2 - scroll wheel
3 - right button

example mouse event binding statements:
Event Format                            Event Description
-----------------                       ---------------------
<Button>, <ButtonPress>                 any button was pressed
<Button-1>, <ButtonPress-1>, <1>        Button 1 on mouse was pressed
<ButtonRelease-1>                       Button 1 on mouse released
<Double-Button-1>                       Button 1 on mouse was double-clicked        
<Triple-Button-1>                       Button 1 on mouse was triple-clicked
<Enter>                                 mouse entered widget area
<Leave>                                 mouse left widget area
<Motion>                                mouse was moved
<B1-Motion>                             mouse was moved with Button 1 held down

'''
# imports ======================================
from tkinter import *
from tkinter import ttk        

# globals ======================================
# prevClick

# functions ====================================
def mouse_press(event):
    global prevClick
    prevClick = event
    typeInfo.configure(text = event.type)
    widgetInfo.configure(text = event.widget)
    numInfo.configure(text = event.num)
    xWidgetInfo.configure(text = event.x) # x coord relative to widget
    yWidgetInfo.configure(text = event.y) # x coord relative to widget
    xScreenInfo.configure(text = event.x_root) # x coord relative to screen
    yScreenInfo.configure(text = event.y_root) # x coord relative to screen      

def draw(event):
    global prevClick
    # to draw a line you need to know starting and ending mouse locations
    canvas.create_line(prevClick.x, prevClick.y,
                       event.x, event.y,
                       width = 4,
                       fill = 'blue')
    prevClick = event
    
# tkinter ======================================    
root = Tk()

# create canvas widget and place it in root window
canvas = Canvas(root, width = 640,
                height = 480,
                background = 'white')
canvas.pack()

# create labelFrame
labelFrameMaster = ttk.Frame(root)
labelFrameMaster.pack()
labelFrame = ttk.Frame(labelFrameMaster)
labelFrame.grid(row = 0, column = 0, columnspan = 7)

typeLabel = ttk.Label(labelFrame, text = 'TYPE  ')
widgetLabel = ttk.Label(labelFrame, text = 'WIDGET  ')
numLabel = ttk.Label(labelFrame, text = 'NUM  ')
xWidgetLabel = ttk.Label(labelFrame, text = 'X-WIDGET  ')
yWidgetLabel = ttk.Label(labelFrame, text = 'Y-WIDGET  ')
xScreenLabel = ttk.Label(labelFrame, text = 'X-SCREEN  ')
yScreenLabel = ttk.Label(labelFrame, text = 'Y-SCREEN  ')

typeLabel.grid(row = 0, column = 0)
widgetLabel.grid(row = 0, column = 1)
numLabel.grid(row = 0, column = 2)
xWidgetLabel.grid(row = 0, column = 3)
yWidgetLabel.grid(row = 0, column = 4)
xScreenLabel.grid(row = 0, column = 5)
yScreenLabel.grid(row = 0, column = 6)

typeInfo = ttk.Label(labelFrame, text = '      ')
widgetInfo = ttk.Label(labelFrame, text = '        ')
numInfo = ttk.Label(labelFrame, text = '     ')
xWidgetInfo = ttk.Label(labelFrame, text = '         ')
yWidgetInfo = ttk.Label(labelFrame, text = '         ')
xScreenInfo = ttk.Label(labelFrame, text = '         ')
yScreenInfo = ttk.Label(labelFrame, text = '         ')

typeInfo.grid(row = 1, column = 0)
widgetInfo.grid(row = 1, column = 1)
numInfo.grid(row = 1, column = 2)
xWidgetInfo.grid(row = 1, column = 3)
yWidgetInfo.grid(row = 1, column = 4)
xScreenInfo.grid(row = 1, column = 5)
yScreenInfo.grid(row = 1, column = 6)

# create event binding for any mouse button clicking on canvas
canvas.bind('<ButtonPress>', mouse_press)

# create event binding for mouse Button 1 being clicked while mouse is moving
canvas.bind('<B1-Motion>', draw)

# tk main loop =================================
root.mainloop()

# main ===============================
def main():
    print('Done.')

if __name__ == '__main__': main()    