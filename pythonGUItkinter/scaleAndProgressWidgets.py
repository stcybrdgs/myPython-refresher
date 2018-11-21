# scale slidebar and progress bar widgets
#
# rem progressbar:
# there are two modes that the progressbar can use:
# determinate - use this mode if you can calculate progress for the operation
# indeterminate - use this mode if you can't estimate progress
#

# imports =========================================
from tkinter import *
from tkinter import ttk

# globals =========================================
stepVal = 0.0
stopVal = 0

# functions =======================================
def startProgress():
	progressbar.start()

def stopProgress():
	progressbar.stop()

def startProgress2():
	global stepVal
	global stopVal
	
	stopVal = 0
	stepVal = 0.0
	progressbar2.start()
	stopValLabel.config(text = str(stopVal))
	stepValLabel.config(text = str(stepVal))

def stopProgress2():
	global stepVal
	global stopVal
	
	stopVal = 1
	stepVal = 0.0
	progressbar2.stop()
	stopValLabel.config(text = str(stopVal))
	stepValLabel.config(text = str(stepVal))

def stepUp():
	global stepVal
	global stopVal
	
	# handle stopVal and stopValLabel
	if(stopVal == 0): progressbar2.stop()
	stopValLabel.config(text = str(stopVal))
	
	# handle stepVal and stepValLabel
	stepVal += 1.0
	if(stepVal == 12.0): stepVal = 0.0
	progressbar2.step()	
	stepValLabel.config(text = str(stepVal))
	progressbar2.config(value = stepVal)
	
# tkinter =========================================
root = Tk()

# indeterminate progressbar ------------------------
progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200) # length in pix
progressbar.grid(row = 0, column = 0, columnspan = 2)
progressbar.config(mode = 'indeterminate')

# use button to call start() and stop() to turn the progressbar on and off
# start button
bttnStart = ttk.Button(root, text = 'Start')
bttnStart.config(command = startProgress)
bttnStart.grid(row = 1, column = 0)

# stop button
bttnStop = ttk.Button(root, text = 'Stop')
bttnStop.config(command = stopProgress)
bttnStop.grid(row = 1, column = 1)

# determinate progressbar --------------------------
progressbar2 = ttk.Progressbar(root, orient = HORIZONTAL, length = 200) # length in pix
progressbar2.grid(row = 2, column = 0, columnspan = 2)

# rem properties
# maximum - the number (float) of steps in current task (default is 100)
# value - the number (float) of steps completed
progressbar2.config(mode = 'determinate', maximum = 11.0, value = 0.0)

# use button to call start() and stop() to turn the progressbar on and off
# start button
bttnStart2 = ttk.Button(root, text = 'Start')
bttnStart2.config(command = startProgress2)
bttnStart2.grid(row = 3, column = 0)

# stop button
bttnStop2 = ttk.Button(root, text = 'Stop')
bttnStop2.config(command = stopProgress2)
bttnStop2.grid(row = 3, column = 1)

# step button
bttnStep = ttk.Button(root, text = 'Step')
bttnStep.config(command = stepUp)
bttnStep.grid(row = 4, column = 0, columnspan = 2)

# stepVal & stopVal labels
stepValLabel = ttk.Label(root, text = str(stepVal))
stopValLabel = ttk.Label(root, text = str(stopVal))
stepValLabel.grid(row = 5, column = 0)
stopValLabel.grid(row = 5, column = 1)

# scale slider bar --------------------------------
# link a scale slider bar to a progress bar
progressbar3 = ttk.Progressbar(root, orient = HORIZONTAL, length = 200) # length in pix
progressbar3.config(mode = 'determinate', maximum = 11.0, value = 0.0)
progressbar3.grid(row = 6, column = 0, columnspan = 2)

# tie progressbar3 to value of scale slider
scaleValue = DoubleVar()  
progressbar3.config(variable = scaleValue)
scale = ttk.Scale(
	root,
	orient = HORIZONTAL,
	length = 200,
	variable = scaleValue,
	from_ = 0.0,
	to = 11.0
	)
scale.grid(row = 7, column = 0, columnspan = 2)

# start tkinter loop
root.mainloop()

# main ============================================
def main():
	print('Done.')
	
if __name__=='__main__': main()