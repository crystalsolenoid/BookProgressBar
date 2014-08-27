import tkinter #GUI
import random #we all know this one

class BookBar:
	#
	#regular constructor
	#
	def __init__(self,tkWindow,sNewTitle,lNewChapters,nProgress=0):
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
		self.nPageOffset = self.nFixPageDisplay(self.lChapters)
		self.nCurrentPage = nProgress
		self.tkLabel = tkinter.Label(tkWindow, text=self.sTitle)
		self.tkCanvas = tkinter.Canvas(tkWindow, width=self.nWidth, height=self.nTotalHeight)
	#
	#calculate how far page 0 is from the start of the introduction
	#will be used to offset the display but preserve page numbers
	#
	def nFixPageDisplay(self, chapters):
		return chapters[0] * -1
	#
	#text-prompted constructor
	#***need to add error checking for user input***
	#
	@classmethod
	def usrMadeBookBar(cls, tkWindow):	
		inBookName = input('name of book: ')
		#walk user through the input process for specifying
		#	the chapter pages of the book
		lChapters = cls.usrInputChapters()
		#checks what page the user is on
		nPage = int(input('what page are you on?: '))
		#return an instance of BookBar
		return(cls(tkWindow, inBookName, lChapters, nPage))
	#
	#generate chapter page list from input
	#(used for usrMadeBookBar)
	#
	@classmethod
	def usrInputChapters(cls):
		#start with an empty list
		lChapters = []
		#
		#check if the book has an introduction and what page it starts on
		#***need to add error checking for user input***
		#
		bIntroduction = input('does it have an introduction? y/n: ')
		if bIntroduction == 'y':
			bActualIntroduction = input('does the introduction start before page 1? y/n: ')
			if bActualIntroduction == 'n':
				#get what page the introduction starts on if it
				#	starts after the page numbering starts 
				nIntro = int(input('what page does it start on?: '))
			else:
				#introductions before 0 are counted, but stored
					#as negative page values
				nIntro = int(input('how long is it?: ')) * -1
		else:
			#the introduction gets a spot in the page list
			#	even if there isn't an introduction, because
			#	that way the chapter numbers still match
			#	their index number
			nIntro = 0
		#put whatever value obtained into the list
		lChapters.append(nIntro)
		#
		#go through and get the start pages of each chapter
		#***need to add error checking for user input***
		#
		nChapters = int(input('how many chapters does it have?: '))
		#for each chapter, get what page it starts on
		for chapter in range(1, nChapters + 1):
			nPage = int(input('what page does chapter '+str(chapter)+' start on?: '))
			#add page number to the page list
			lChapters.append(nPage)
		#
		#get what page the book ends on
		#***need to add error checking for user input***
		#
		nEndPage = int(input('what page does chapter '+str(nChapters)+' end on?: '))
		#add page of end of book to page list
		lChapters.append(nEndPage)
		#debug
		print(str(lChapters)+" debug")
		#returns list to be used in BookBar constructor
		return(lChapters)
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
			x0 = self.nPadding + ((nStart+self.nPageOffset) * nPageScale)
			y0 = self.nPadding + self.nBookmarkOffset
			x = self.nPadding + ((nEnd+self.nPageOffset) * nPageScale)
			y = self.nPadding + self.nBookmarkOffset + self.nBarHeight
			sColor = self.sSelectColor(sColor) #generates a random color
			#
			self.tkCanvas.create_rectangle(x0, y0, x, y, fill=sColor)
		#
		#draw the bookmark (current progress)
		#
		x0 = self.nPadding + ((self.nCurrentPage+self.nPageOffset) * nPageScale) - 1
		y0 = self.nPadding
		x = self.nPadding + ((self.nCurrentPage+self.nPageOffset) * nPageScale) + 1
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