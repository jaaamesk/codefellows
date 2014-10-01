class Library(object):
	def __init__(self):
		self.shelf_list = []
		self.book_list = []

	def callShelf(self):
		print "The shelves are categorized by: "
		for x in self.shelf_list:
			print x
		print "for a total of ", len(self.shelf_list), "shelves in the library."

	def callBook(self):
		print "The books that we currently carry include: "
		for y in self.book_list:
			print y

class Shelf(object):
	def __init__(self, shelf, lib):
		self.shelf = shelf
		self.bINshelf = []
		lib.shelf_list.append(self.shelf)

	def shelfstuff(self):
		print "The %s shelf contains the following literature: " % self.shelf
		for z in self.bINshelf:
			print z


class Book(object):
	def __init__(self, book, lib):
		self.book = book
		lib.book_list.append(self.book)

	def enshelf(self, toshelf):
		toshelf.bINshelf.append(self.book)



	def unshelf(self, fromshelf):
		fromshelf.bINshelf.remove(self.book)



JK = Library()

aTOh = Shelf("A to H", JK)
iTOq = Shelf("I to Q", JK)
rTOz = Shelf("R to Z", JK)


animal = Book("Animals", JK)
animal.enshelf(aTOh)
brisket = Book("Briskets", JK)
brisket.enshelf(aTOh)

ibs = Book("Irritable Bowel Syndromes", JK)
ibs.enshelf(iTOq)
laugh = Book("Laughing Countrymen", JK)
laugh.enshelf(iTOq)

rage = Book("RageCage", JK)
rage.enshelf(rTOz)
apple = Book("Apples and Gophers", JK)
apple.enshelf(rTOz) #its in the wrong section! Will fix in line
zed = Book("Zed's Dead", JK)
zed.enshelf(rTOz)


JK.callShelf()
JK.callBook()

aTOh.shelfstuff()
iTOq.shelfstuff()
rTOz.shelfstuff()

apple.unshelf(rTOz)
apple.enshelf(aTOh)

print "\nLet's try that one more time."
print " "

aTOh.shelfstuff()
iTOq.shelfstuff()
rTOz.shelfstuff()
