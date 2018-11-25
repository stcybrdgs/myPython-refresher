# canvasWidget.py
#
# the canvas widget gives you space on which to draw and organize
# various shapes, images, and even other widgets
#
# imports ====================================
from tkinter import *
from tkinter import ttk
# canvas widgets are not part of ttk

# globals ====================================
changeLineCount = 0

# functions ==================================
def radioSelect():
	radioColor = color.get()
	canvas.itemconfig(line, fill = radioColor)
	infoStr = 'The color is: ' + radioColor
	infoContent.configure(text = infoStr)
	
def changeLine():
	global changeLineCount
	if(changeLineCount == 0): 
		changeLineCount += 1
		canvas.coords(line, 0, 0, 320, 240, 640, 0)
	elif(changeLineCount == 1):
		changeLineCount += 1
		canvas.coords(line, 0, 480, 320, 240, 640, 480)
	elif(changeLineCount == 2):
		changeLineCount += 1
		canvas.coords(line, 320, 0, 320, 480)
	elif(changeLineCount == 3):
		changeLineCount += 1
		canvas.coords(line, 0, 240, 640, 240)
	elif(changeLineCount == 4):
		changeLineCount = 0
		canvas.coords(line, 160, 360, 480, 120,)		

def smoothSelect():
	if(smoothIt.get() == 'Normal'):
		#smoothIt.set('Smooth')
		canvas.itemconfigure(line, smooth = 'True')
	else:
		smoothIt.set('Normal')
		canvas.itemconfigure(line, smooth = False)
	
	print(smooth.get())
	
# tkinter ====================================
root = Tk()

# create a canvas
canvas = Canvas(root)
canvas.grid(row = 0, column = 0, columnspan = 2)

# specify canvas size:
canvas.config(width = 640, height = 480)
line = canvas.create_line(
	# (x,y,x,y) coordinate pairs, corner to corner
	160, 360, 480, 120,
	fill = 'blue',
	width = 5
	)
	
# rem when you create an item on the canvas, the create method
# returns an ID that you can use to reference the item later to
# make changes. If you won't need to modify, then you can ignore
# the ID, but if you will need to make mods, then you want to
# capture the ID in a variable (ie, we used 'canvas' as our var
# in the script above)

# change the line color to red
canvas.itemconfig(line, fill = 'blue')

# radio options
radioFrame = ttk.Frame(root)
radioFrame.grid(row = 1, column = 0, columnspan = 2)
color = StringVar()
color.set('Blue')
ttk.Radiobutton(radioFrame, text = 'Blue', variable = color, value = 'Blue', command = radioSelect).pack() 
ttk.Radiobutton(radioFrame, text = 'Red', variable = color, value = 'Red', command = radioSelect).pack()
ttk.Radiobutton(radioFrame, text = 'Orange', variable = color, value = 'Orange', command = radioSelect).pack()
ttk.Radiobutton(radioFrame, text = 'Yellow', variable = color, value = 'Yellow', command = radioSelect).pack()
ttk.Radiobutton(radioFrame, text = 'Green', variable = color, value = 'Green', command = radioSelect).pack()
ttk.Radiobutton(radioFrame, text = 'Brown', variable = color, value = 'Brown', command = radioSelect).pack()

# check box option
checkbox = ttk.Checkbutton(root, text = 'Smooth')
checkbox.grid(row = 2, column = 0)
state = StringVar()
state.set('Normal')
checkbox.config(
	variable = state,
	onvalue = 'Smooth',
	offvalue = 'Normal'
)
checkbox.configure(command = stateSelect)

# button options
button = ttk.Button(root, text = 'Change Line', padding = (10, 10))
button.grid(row = 2, column = 1)
button.configure(command = changeLine)

# make a frame under the canvas for showing canvas info
infoFrameLft = ttk.Frame(root)
infoFrameRt = ttk.Frame(root)
infoFrameLft.grid(row = 3, column = 0)
infoFrameRt.grid(row = 3, column = 1)

# get the line coordinates
infoHeader = ttk.Label(infoFrameLft, text = 'CANVAS INFO:  ')
infoHeader.pack()
infoContent = ttk.Label(infoFrameRt, text = 'The color is blue')
infoContent.pack()

	
# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()