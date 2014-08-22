#import libraries
import tkinter #GUI library
import random

#import other files from this project
from BookBar import *
#i should probably make it import BookBar
#	in a way other than "import *" because
#	that can get messy but for now it'll be fine


#creates the window we're gonna render stuff on
window=tkinter.Tk()


#
#create our BookBars
#

#list to store instances of the BookBar class in
dBooks=[]

#how the BookBar creation works:
#BookBar(tkinter window it's assigned to,
#	book title(a string),
#	list of chaper pages)
#
#the zeroith value in the list of chapter pages
#	is the start of the book's introduction.
#	if the introduction starts before page 0
#	(for example at page iv), i just set it to 0.
#value 1 and onward are when the table of contents
#	says that chapter starts.
#	so list[3] would be the page chapter 3 starts on
#
#it'd be nice if we could detect when there's no introduction
#	and not draw the introduction in that case

#books Quin's currently reading for school
dBooks.append(BookBar(window,
	'the emotional life of your BRAIN',
	[0,1,13,43,67,91,113,137,161,177,199,225,253]))

dBooks.append(BookBar(window,
	'general chemistry',
	[0,1,34,68,111,151,192,241,294,360,395,449,498,
	557,602,665,697,745,784,819,863,917,976,1031,1069,
	1111,1147,1208,1266]))

dBooks.append(BookBar(window,
	'geoffrey of monmouth',
	[53,75,107,149,170,186,212,262,285]))

dBooks.append(BookBar(window,
	'ibn fadlan and the land of darkness',
	[0,1,59,93,201]))

dBooks.append(BookBar(window,
	'agricola and germany',
	[0,1,35,63]))

dBooks.append(BookBar(window,
	'the holy greyhound',
	[1,9,14,25,37,68,83,89,124,145,157,171]))

#
#set the book progress for things I've started reading
#
#the emotional life of your BRAIN
dBooks[0].setProgress(57)
#general chemistry
dBooks[1].setProgress(111)

#
#tkinter button actions
#

#addBook isn't implemented yet
def addBook():
	sBookName=input('name of book: ')
	nBookPages=int(input('number of pages: '))
	nProgress=0

#goes through each book and tells it to draw itself
def canvasRefresh():
	for book in dBooks:
		book.renderBook()

#create the actual buttons
buttonAddBook=tkinter.Button(window,text='Add A Book (not yet implemented)',command=addBook)
buttonRefresh=tkinter.Button(window,text='Refresh Canvas',command=canvasRefresh)

#define other display features
# text=tkinter.Text(window, width=1, height=1)

#tk renders things automatically when you pack them
buttonAddBook.pack()
buttonRefresh.pack()
for book in dBooks:
	book.pack()

#render the book bars
canvasRefresh()

#main loop
window.mainloop()

#(program ends when you close the tkinter window)