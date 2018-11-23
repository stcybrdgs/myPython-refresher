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


# functions ==================================


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
text.insert('1.0', 'This is the default text for this text widget.')

# TAGS ---------------------------------------
# create a tag that spans the first word in the text box
text.tag_add('my_tag', '1.0', '1.0 wordend') # (nameOfTag, startLoc, endLoc)

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

# MARKS --------------------------------------


# tkinter loop
root.mainloop()

# main() ====================================
def main():
	print('Done.')
	
if __name__ == '__main__': main()