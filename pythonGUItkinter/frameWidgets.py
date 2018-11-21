# widgetsWithFrames.py
#
# frames are one of the fundamental widgets you'll use when organizing a
# tkinter GUI. A frame is simply a rectangular region on the screen, but it
# is useful because it can acta as a parent and a geometry manager for
# the other widgets contained within it, so it can be used for organizational
# purposes within your root tk instance.
# Another benefit of using frames is that a different type of geometry manager
# may be used in each frame.


# imports ========================================
from tkinter import *
from tkinter import ttk

# functions ======================================
def destroyNuWindow():
	nuWin.destroy()
	
def popup():
	# testWin command functions ------------------
	def testWinTop():
		testWin.lift()
	
	def testWinBottom():
		testWin.lower()
		
	def testWinLower():
		testWin.lower(root)
		
	def testWinHigher():
		testWin.lift(root)
		
	# visWin command functions -------------------
	def testWinNormal():
		testWin.state('normal')
		
	def testWinIconify():
		testWin.iconify()
		
	def testWinIconic():
		testWin.state('iconic')
	
	def testWinWithdrawn():
		testWin.state('withdrawn')
		
	def testWinZoomed():
		testWin.state('zoomed')
		
	# open the test window and place it on top
	testWin = Toplevel(root)
	testWin.title('Test Window') # name the window frame
	testWin.lift() # put window at top of window stack
	
	# open the control window and place it on top
	controlWin = Toplevel(root)
	controlWin.title('Control Window')
	controlWin.lift()
	
	# rem position functions
	# window.lower() # put window at bottom of window stack
	# window.lower(root) # put window at loc just below root window
	# window.lift(root) # put window at loc just above root window
	
	# rem state functions (visibility)
	# window state: choose 'normal', 'icon', 'iconic', 'withdrawn', or 'zoomed'
	# rem 'zoomed' will fill the screen with new window
	#      'withdrawn' will hide the window completely
	#      'iconic' will hide window but show it as an option in the taskbar
	
	# position frame --------------------
	posFrame = ttk.Frame(controlWin)
	posFrame.grid(row = 0, column = 0)
	posFrame.config(
		width = 100,
		relief = RIDGE,
		padding = (10, 10)
	)
	posHeader = ttk.Label(posFrame, text = 'Position Controls')
	posHeader.pack()
	
	# position buttons
	topBttn = ttk.Button(posFrame, text = 'Top')
	bottomBttn = ttk.Button(posFrame, text = 'Bottom')
	lowerBttn = ttk.Button(posFrame, text = 'Lower')
	higherBttn = ttk.Button(posFrame, text = 'Higher')
	emptyBttn = ttk.Button(posFrame, text = 'Empty')
	topBttn.pack()
	bottomBttn.pack()
	lowerBttn.pack()
	higherBttn.pack()
	emptyBttn.pack()
	topBttn.config(command = testWinTop)
	bottomBttn.config(command = testWinBottom)
	lowerBttn.config(command = testWinLower)
	higherBttn.config(command = testWinHigher)
			
	# visibility frame --------------------
	visFrame = ttk.Frame(controlWin)
	visFrame.grid(row = 0, column = 1)
	visFrame.config(
		width = 100,
		relief = RIDGE,
		padding = (10, 10)
	)
	visHeader = ttk.Label(visFrame, text = 'Visibility Controls')
	visHeader.pack()
	
	# visibility buttons
	normalBttn = ttk.Button(visFrame, text = 'Normal')
	iconifyBttn = ttk.Button(visFrame, text = 'Iconify')
	iconicBttn = ttk.Button(visFrame, text = 'Iconic')
	withdrawnBttn = ttk.Button(visFrame, text = 'Withdrawn')
	zoomedBttn = ttk.Button(visFrame, text = 'Zoomed')
	normalBttn.pack()
	iconifyBttn.pack()
	iconicBttn.pack()
	withdrawnBttn.pack()
	zoomedBttn.pack()
	normalBttn.config(command = testWinNormal)
	iconifyBttn.config(command = testWinIconify)
	iconicBttn.config(command = testWinIconic)
	withdrawnBttn.config(command = testWinWithdrawn)
	zoomedBttn.config(command = testWinZoomed)	

# tkinter ========================================
root = Tk()
root.title('My App')

# re: frame relief, there are 6 kinds: flat, raised, sunken, solid, ridge, groove
frame = ttk.Frame(root)
frame.pack()
frame.config(
	height = 100,
	width = 200,
	relief = RIDGE,
	padding = (30,15) # (x direction, y direction)
	)

button = ttk.Button(frame, text = 'Click Me')
button.grid(row = 0, column = 0)

destroyBttn = ttk.Button(frame, text = 'Destroy NuWindow')
destroyBttn.grid(row = 1, column = 0)
destroyBttn.config(command = destroyNuWindow)

# the LabelFrame widget is a type of frame;
# it is a container used to gruop other widgets together,
# which has an optional label wchih may be a plain text string or another widget
# rem you can't use relief with LabelFrame
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

# additional top-level windows
# Each top-level window you create is its own Tk widget object, which you can
# use as the parent and geometry manager for other widgets.
# You can use them to create new GUI sections for your program or to just
# display simple popup messages for the user.
# rem top-level window are not part of the themed widget set, so you don't
#     need ttk for them.
#
# here, we're using the Click Me button to trigger the new top level window
button.config(command = popup)

# the geometry method ----------------------------
# By default, when an empty window is created it's 200 by 200 pixels.
# If we want to change the size and/or relocate the window programmatically,
# we can do so using the geometry method.
# The geometry method takes one parameter, which is a string containing
# the new width and height in pixels of the window, ie:
# window.geomterty('WIDTHxHEIGHT+X+Y')
# where X and Y represent the location in pixels of the window's top left corner
# relative to the top left corner of the screen.
nuWin = Toplevel(root)
nuWin.title('Nu Window') # name the window frame
nuWin.lift() # put window at top of window stack
nuWin.geometry('640x480+50+50')

# you can specify whether or not the user is allowed to resize the window
nuWin.resizable('False', 'True') # (x direction, y direction)

# you can specify to what extent the user can resize the window
nuWin.maxsize(800, 600) # (x value in pixels, y value in pixels)
nuWin.minsize(400, 200) # (x value in pixels, y value in pixels)

# you can programatically close top-level windows by calling the destroy() method
# rem the destroy() method can be called on all kinds of widgets, not just windows
#     the destroy() method will affect not only the target window but also all of its children


root.mainloop()

# main ===========================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()