# msgBoxAndDialogs.py
#
# you can use prebuilt message box methods to easily create
# pop-up alerts for the user. You can also use the file dialogue and
# color chooser methods to present the user with familiar selection menus
# from their operating system.
#
# These dialogues and message boxes are not regular TK widgets. You only
# need to import the message box module from the TKinter package

# imports  =================================
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser

# tkinter  =================================
messagebox.showinfo(title = 'A Message from God',
					message = 'Get your $h!t together!')

# types of messagebox include:
# informational:
#    showinfo()
#    showwarning()
#    showerror()
# questions (return True or Fals depending on user response):
#     askyesno()
#     askokcancel()
#     askretrycancel()
#     askyesnocancel()
#     askquestion()
# Filedialog types:
#     askdirectory()
#     asksaveasfile(mode)
#     asksaveasfilename()
#     askopenfile(mode)
#     askopenfiles(mode)
#     askopenfilename()
#     askopenfilenames()

# askyesno message:
messagebox.askyesno(title = 'Hungry?', message = 'Have you eaten?')

# prompt the user to browse for a file or dialogue path
filename = filedialog.askopenfile()
# retrieve name of selected file:
# print(filename.name)

'''
when you set off a Markdown section sith triple quotes,
it will exist as a multiline comment and won't run as code
'''

# open the colorchooser
colorchooser.askcolor(initialcolor = '#FFFFFF')
# after the user makes a selection in the colorchooser, it returns
# a list with two items:
#     the RGB of the selected color
#     a string containing the hex representation of the selected color

# main =====================================
def main():
	print('Done')

if __name__ == '__main__' : main()	



