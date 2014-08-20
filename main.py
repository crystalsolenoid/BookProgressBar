import tkinter #GUI
import random #we all know this one
from book_class_pretty import *



#creates the window we're gonna render stuff on
window=tkinter.Tk()

#ex={'title':[[1st chapter starts,2nd,3rd,etc.],current page]}
# dBooks={'geoffrey of monmouth':[[53,75,107,149,170,186,212,262,285],154]}
# dBooks=[[[0,1,13,43,67,91,113,137,161,177,199,225,253],43,'the emotional life of your BRAIN',tkinter.Canvas(window,width=windowWidth,height=nTotalHeight),tkinter.Label(window,text='the emotional life of your BRAIN')],[[0,1,34,68,111,151,192,241,294,360,395,449,498,557,602,665,697,745,784,819,863,917,976,1031,1069,1111,1147,1208,1266],68,'general chemistry',tkinter.Canvas(window,width=windowWidth,height=nTotalHeight),tkinter.Label(window,text='general chemistry')],[[53,75,107,149,170,186,212,262,285],0,'geoffrey of monmouth',tkinter.Canvas(window,width=windowWidth,height=nTotalHeight),tkinter.Label(window,text='geoffrey of monmouth')],[[0,1,59,93,201],0,'ibn fadlan and the land of darkness',tkinter.Canvas(window,width=windowWidth,height=nTotalHeight),tkinter.Label(window,text='ibn fadlan and the land of darkness')],[[0,1,35,63],0,'agricola and germany',tkinter.Canvas(window,width=windowWidth,height=nTotalHeight),tkinter.Label(window,text='agricola and germany')],[[1,9,14,25,37,68,83,89,124,145,157,171],0,'the holy greyhound',tkinter.Canvas(window,width=windowWidth,height=nTotalHeight),tkinter.Label(window,text='the holy greyhound')]]

dBooks=[]

dBooks.append(BookBar(window,'the emotional life of your BRAIN',[0,1,13,43,67,91,113,137,161,177,199,225,253]))

# BookBar(window,'the emotional life of your BRAIN',[0,1,13,43,67,91,113,137,161,177,199,225,253])

#button actions
def addBook():
	sBookName=input('name of book: ')
	nBookPages=int(input('number of pages: '))
	nProgress=0
def canvasRefresh():
	for book in dBooks:
		book.renderBook()

#render a book progress bar
# def renderBook(book,x0,y0):
# 	sColor=''#initializes the random color
# 	nLastPage=book[0][len(book[0])-1]#find out how long the total bar is
# 	nPageScale=min((windowWidth-nPadding*2)/nLastPage,1.5)
# 	for nChapter in range(len(book[0])):#iterate through each chapter
# 		if nChapter==0:#the introduction starts at page 0
# 			nStart=0
# 		else:#gets the first page at the chapter
# 			nStart=(book[0][nChapter-1])*nPageScale
# 		nEnd=(book[0][nChapter]-1)*nPageScale#gets the last page of the chapter
# 		sColor=sSelectColor(sColor)#generates a random color
# 		book[3].create_rectangle(x0+nStart,y0+nBookmarkOffset,x0+nEnd,y0+nBookmarkOffset+nBarHeight,fill=sColor)#draw that part of the bar in a random color
# 		book[3].create_rectangle(x0+book[1]*nPageScale-1,y0,x0+book[1]*nPageScale+1,y0+nBarHeight+nBookmarkOffset*2,fill='red',outline='red')#draw the bookmark (current progress)

# def sSelectColor(sOldColor):
# 	sNewColor=random.choice(['cyan','blue','green','pink','orange','magenta','yellow'])
# 	while sNewColor==sOldColor:
# 		sNewColor=random.choice(['cyan','blue','green','pink','orange','magenta','yellow'])
# 	return sNewColor



#define the buttons
buttonAddBook=tkinter.Button(window,text='Add A Book',command=addBook)
buttonRefresh=tkinter.Button(window,text='Refresh Canvas',command=canvasRefresh)

#define display features
# text=tkinter.Text(window, width=1, height=1)

#renders buttons automatically
buttonAddBook.pack()
# text.pack()
# canvas.pack()
buttonRefresh.pack()
for book in dBooks:
	book.pack()
	print("hix")

#main loop
window.mainloop()


#keeps the window from closing instantly
# window.mainloop()