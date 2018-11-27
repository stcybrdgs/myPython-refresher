# canvasWidget_2.py
#

# imports ====================================
from tkinter import *
from tkinter import ttk
# canvas widgets are not part of ttk

# globals ====================================

# functions ==================================
	
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

# draw a rectangle
# the xy pairs represent top-left and bottom-right corners
rect = canvas.create_rectangle(160, 120, 420, 260)
canvas.itemconfigure(rect, fill = 'green')

# draw an oval
# xy pairs represent top-left and bottom-right corners of a bounding box
oval = canvas.create_oval(120, 120, 210, 230)

# draw an arc
# an arc is just a piece of the oval from 0 to 90 degrees
# within a bound box where the box is represented by xy pairs
# just like those used for rectangle and oval
arc = canvas.create_arc(160, 1, 480, 240)
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'brown')

# draw a polygon
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')

# add text to the canvas
text = canvas.create_text(320, 240, text = 'Python is awesome!',
						  font = ('Courier', 32, 'bold'))

# add a logo
logo = PhotoImage(file = 'python_logo.gif')
image = canvas.create_image(320, 240, image = logo)

# images are added to the canvas in the order that they are created, with
# the most recently created items appearing on top; to move shapes,
# you can use lift() and lower()
canvas.lift(text)
canvas.lower(rect)

# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()