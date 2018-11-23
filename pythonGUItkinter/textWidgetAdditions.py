# textWidgetAdditions.py
# add tags, marks, images, and widgets to the text widget
# rem tags describe a range or collection of characters
# rem marks specify a location between two characters in the text widget
# rem we can use tags and marks to change properties such as font and color
#     as well as to control where to insert or delete text

# imports ====================================
from tkinter import *
from tkinter import ttk
# the text widget is not a themed widget, btw

# global =====================================
tagString = 'empty'
tagCount = 0
recentTag = 'empty'

# functions ==================================
def submitHandler():
	global tagCount
	global recentTag
	
	# increment tagCount
	tagCount += 1
	
	# get start loc and end loc of most recent tag
	tagString = text.tag_ranges(recentTag)
	
	# make recent end loc to be the start loc of the new tag
	# and convert it to float and add .1 for the ending character space
	startVal = float(str(tagString[1])) + .1 
	
	# convert starting loc to start and end strings
	nuTagName = 'tag' + str(tagCount)
	recentTag = nuTagName
	nuTagStart = str(startVal)
	nuTagEnd = nuTagStart + ' wordend'
	
	if( tagOp.get() == 'Add' ):
		text.tag_add(nuTagName, nuTagStart, nuTagEnd) # (nameOfTag, startLoc, endLoc)
		text.tag_configure(nuTagName, background = 'yellow')
		label.config(text = 'start: ' + nuTagStart + ', end: ' + nuTagEnd)
	elif( tagOp.get() == 'Remove' ):
		label.config(text = tagString)
	elif( tagOp.get() == 'Replace' ):
		label.config(text = tagString)
	elif( tagOp.get() == 'Highlight' ):
		label.config(text = tagString)
	elif( tagOp.get() == 'Get Range' ):
		label.config(text = tagString)

# tkinter ====================================
root = Tk()

# create text field
text = Text(root,
			width = 40,
			height = 10,
			relief = SOLID,
			wrap = 'word'
			)
text.pack()
text.insert('1.0', 'This is the default text for this text widget.\nThere are several lines of it.\nEnding with this one')

# TAGS ---------------------------------------
# create a tag that spans the first word in the text box
text.tag_add('my_tag', '1.0', '1.0 wordend') # (nameOfTag, startLoc, endLoc)
recentTag = 'my_tag'

# put yellow highlight on my_tag
text.tag_configure('my_tag', background = 'yellow')

# rem you can create multiple tags for the same span of text
# rem if there is a conflict in applying attributes to the tags, then
#     those conflicts will be resolved according to a priority system where the
#     most recently applied tag receives the highest priority
# rem you can change the priority of the tags with the methods
#     tag_raise() and tag_lower()
# rem you can remove a tag from a section of text with the method
#     tag_remove('nameOfTagToRemove', 'startIndex', 'endIndex(nonInclusive)')
# rem to find out range of chars included in a tag, use tag_ranges('nameOfTag')
# rem to get a list of all the tags that exist in your text, use tag_names()
# rem to find out a tag name that covers a given character, ex: tag_names('1.0')
# rem to replace the tag and its text with a new tag and new text:
#     text.replace('my_tag.first', 'my_tag.last', 'replacement text'), where
#     .first is the first char the text range and .last is the last char of the range
# rem to delete a tag: text.tag_delete('my_tag')

# radio button
# each radio button is its own object, and they're all tied together by a common variable
ttk.Label(root, text = 'TAG OPS:').pack()
tagOp= StringVar()
tagOp.set('Add')
ttk.Radiobutton(root, text = 'Add', variable = tagOp, value = 'Add').pack()
ttk.Radiobutton(root, text = 'Remove', variable = tagOp, value = 'Remove').pack()
ttk.Radiobutton(root, text = 'Replace', variable = tagOp, value = 'Replace').pack()
ttk.Radiobutton(root, text = 'Highlight', variable = tagOp, value = 'Highlight').pack()
ttk.Radiobutton(root, text = 'Get Range', variable = tagOp, value = 'Get Range').pack()
button = ttk.Button(root, text = 'Submit')
button.pack()
button.config(command = submitHandler)
label = ttk.Label(root, text='Tag Ops Output')
label.pack()


# MARKS --------------------------------------
# marks specify a single position which exist between two characters
# to get a list of the marks that are present in a text widget:
# text.mark_names()
# where two of the names returned will be marks that Tk automatically keeps track of:
#    'insert' - the current index of the insertion cursor
#    'current' - the index that is currently under the mouse position
# rem you can create and modify the location of marks using the mark_set() method:
#     text.mark_set('my_mark', 'end')
# rem marks have a thing called gravity to determine whether the mark should shift
#     to the left or to the right if surrounding text gets manipulated by some
#     other aspect of the program. To configure the gravity for a mark, we use
#     the mark_gravity() method:
#     text.mark_gravity('my_mark', 'right'), where you can specify either left or right
# rem you can remove a mark with unset():
#     text.mark_unset('my_mark')



# tkinter loop
root.mainloop()

# main() ====================================
def main():
	global recentTag
	print(recentTag)
	print('Done.')
	
if __name__ == '__main__': main()