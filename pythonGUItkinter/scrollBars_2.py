# scrollBars.py
#
# if you GUI includes widgets that are too large to view in the
# available space, then you can include a scroll bar to enable the user
# to selectively view different sections of it.
# in Tk, scrollbars are their own unique widgets, rather than just
# being a sub feature of other widgets

# imports ====================================
from tkinter import *

	
# tkinter ====================================
root = Tk()

# create a canvas with x and y scroll bars
canvas = Canvas(root, scrollregion = (0, 0, 640, 480), bg = 'white')
xscroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = canvas.xview)
yscroll = ttk.Scrollbar(root, orient = VERTICAL, command = canvas.yview)
canvas.config(xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

canvas.grid(row = 1, column = 0)
xscroll.grid(row = 2, column = 0, sticky = 'ew')
yscroll.grid(row = 1, column = 1, sticky = 'ns')

def canvas_click(event):
	# event.x & event.y find the xy locs where click occurred
	# while canvas.canvasx() and canvas.canvasy() translate
	# the click area if it lies outside original canvas scroll region
	x = canvas.canvasx(event.x) # find x loc where click occurred
	y = canvas.canvasy(event.y) # find y loc where click occurred
	canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')
	
# if user clicks canvas, call canvas_click(event)
# and pass in the xy location where the click occurred
canvas.bind('<1>', canvas_click)

# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()