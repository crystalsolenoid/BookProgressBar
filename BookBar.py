import tkinter #GUI
import random #we all know this one

class BookBar:
	#
	#regular constructor
	#
	def __init__(self,tkWindow,sNewTitle,lNewChapters):
		#
		#generating dimensions for the progress bars
		#
		self.nWidth = 300
		self.nBookmarkOffset = 5
		self.nBarHeight = 10
		self.nPadding = 5
		self.nTotalHeight = (self.nBookmarkOffset * 2) + self.nBarHeight + (self.nPadding * 2)
		#
		self.sTitle = sNewTitle
		self.lChapters = lNewChapters
		self.nCurrentPage = 0
		self.tkLabel = tkinter.Label(tkWindow, text=self.sTitle)
		self.tkCanvas = tkinter.Canvas(tkWindow, width=self.nWidth, height=self.nTotalHeight)
	#
	#text-prompted constructor
	#
	@classmethod
	def usrMadeBookBar(cls,tkWindow):	
		inBookName=input('name of book: ')
		inBookLength=int(input('number of pages: '))
		lLength=[0,inBookLength]
		return(cls(tkWindow,inBookName,lLength))
	#
	#draw the progress bar onto the tkinter canvas
	#
	def renderBook(self):
		sColor = '' #initializes the random color
		nLastPage = self.lChapters[len(self.lChapters) - 1] #find out how long the total bar is
		nPageScale = min((self.nWidth - self.nPadding * 2) / nLastPage, 1.5)
		#
		#iterate through each chapter
		#
		for nChapter in range(len(self.lChapters)):
			#
			#find out what our page bounaries are for this chapter
			#
			if nChapter == 0: #the introduction starts at page 0
				nStart = 0
			else: #gets the first page at the chapter
				nStart = self.lChapters[nChapter - 1]
			nEnd = self.lChapters[nChapter] - 1 #gets the last page of the chapter
			#
			#draw that part of the bar in a random color
			#
			x0 = self.nPadding + (nStart * nPageScale)
			y0 = self.nPadding + self.nBookmarkOffset
			x = self.nPadding + (nEnd * nPageScale)
			y = self.nPadding + self.nBookmarkOffset + self.nBarHeight
			sColor = self.sSelectColor(sColor) #generates a random color
			#
			self.tkCanvas.create_rectangle(x0, y0, x, y, fill=sColor)
		#
		#draw the bookmark (current progress)
		#
		x0 = self.nPadding + (self.nCurrentPage * nPageScale) - 1
		y0 = self.nPadding
		x = self.nPadding + (self.nCurrentPage * nPageScale) + 1
		y = self.nPadding + self.nBarHeight + (self.nBookmarkOffset * 2)
		#
		self.tkCanvas.create_rectangle(x0, y0, x, y, fill = 'red',outline = 'red')
	#
	#random color selecter for renderBook()
	#
	def sSelectColor(self,sOldColor):
		#sOldColor is the previous color generated with this function
		#list of colors it'll pick from
		#(possibly put this as a class trait later)
		lColors=['cyan','blue','green','pink','orange','magenta','yellow']
		#pick a random color from the list
		sNewColor = random.choice(lColors)
		#make sure that there isn't two of the same color in a row
		#it only goes through this loop when it detects a repeat
		while sNewColor == sOldColor:
			sNewColor = random.choice(lColors)
		return sNewColor
	#
	#changes the page you're currently on
	#
	def setProgress(self,nNewPage):
		self.nCurrentPage = nNewPage
	#
	#pack to window
	#
	def pack(self):
		self.tkLabel.pack()
		self.tkCanvas.pack()