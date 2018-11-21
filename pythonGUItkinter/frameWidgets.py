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
def popup():
	# open the test window and place it on top
	testWin = Toplevel(root)
	testWin.title('Test Window') # name the window frame
	testWin.lift() # put window at top of window stack
	
	# open the control window and place it on top
	controlWin = Toplevel(root)
	controlWin.title('Control Window')
	controlWin.lift()
	
	# position frame
	
	# position buttons
	topBttn = ttk.Button(controlWin, text = 'Top')
	bottomBttn = ttk.Button(controlWin, text = 'Bottom')
	lowerBttn = ttk.Button(controlWin, text = 'Lower')
	higherBttn = ttk.Button(controlWin, text = 'Higher')
		
	# visibility frame	
	# visibility buttons
	normalBttn = ttk.Button(controlWin, text = 'Normal')
	iconBttn = ttk.Button(controlWin, text = 'Icon')
	iconicBttn = ttk.Button(controlWin, text = 'Iconic')
	withdrawnBttn = ttk.Button(controlWin, text = 'Withdrawn')
	zoomedBttn = ttk.Button(controlWin, text = 'Zoomed')
	
	
	# window.lower() # put window at bottom of window stack
	# window.lower(root) # put window at loc just below root window
	# window.lift(root) # put window at loc just above root window
	
	# window state: choose 'normal', 'icon', 'iconic', 'withdrawn', or 'zoomed'
	# rem 'zoomed' will fill the screen with new window
	#      'withdrawn' will hide the window completely
	#      'iconic' will hide window but show it as an option in the taskbar
	

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
button.grid()

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


root.mainloop()

# main ===========================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()