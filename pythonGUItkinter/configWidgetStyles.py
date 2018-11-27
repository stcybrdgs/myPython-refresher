# configWidgetStyles.py
#
# styles describe how widgets will appear depending on their state
# rem a widget may possess more than one of the ten possible state
# attribute at any point in time depending on how the widget
# has been configured and how the user is interacting with it:
# active      background    disabled   readonly    focus
# alternate   pressed       invalid    selected    hover
#
# tk also offers collections of widget styles that allow you to make
# your GUI's widgets look consistent; alternatively, you may even
# reate your own widget styles

# imports  =================================
from tkinter import *
from tkinter import ttk

# globals ==================================


# functions ================================


# tkinter  =================================
root = Tk()
button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')
button1.pack()
button2.pack()
style = ttk.Style()

# returns all style themes:
print(style.theme_names())

# theme results are:
#     winnative, clam, alt, default, classic, vista, xpnative

# use the 'classic' theme
style.theme_use('clam')

# to find out the namd of the default style that a widget uses, call the
# w info class method on an object:
print('button 1 default style is: ', button1.winfo_class())

# change the theme as used by the default style
style.configure('TButton', foreground = 'green')

# create new style called Alarm, TButton
style.configure('Alarm.TButton',
				foreground = 'orange',
				font = ('Arial', 12, 'bold'))

# use new style on button2
button2.config(style = 'Alarm.TButton')


style.map('Alarm.TButton',
		  foreground = [
			('pressed', 'pink'),
			('disabled', 'grey')
			]
		  )

# disable button2
button2.state(['disabled'])

# the layout method
# print the list of elements within the TButton style
print('\nstyle.layout(\'TButton\')\n', style.layout('TButton'))

# element_options
# learn about the options that are available for the elements of any widget
# so that you can fully customize their appearance with custom styles
print('\nstyle.element_options(\'Button.label\')\n', style.element_options('Button.label'))

# root main loop
root.mainloop()

# main =====================================
def main():
	print('Done')

if __name__ == '__main__' : main()	



