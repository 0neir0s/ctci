class Library(object):

    def __init__(self):
        self.books = {}
        self.members = {}
        self.borrowedBooks = {} # Mapping book-id to member-id
        self.membersWithBooks = set()
    
    def borrow(self, memid, bookid):
        """ If member is valid, get him the book """
        if memid not in self.members or bookid not in self.books:
            raise Exception("Incorrect details")
        if memid in self.membersWithBooks:
            raise Exception("Return the book first")
        if bookid in self.borrowedBooks:
            raise Exception("Book already in circulation")
        self.borrowedBooks[bookid] = memid
        self.membersWithBooks.add(memid)

    def return(self, memberid, bookid):
        """ Return the book with the member back to the library """
        if memid not in self.members or bookid not in self.books:
            raise Exception("Incorrect details")
        if memid not in self.membersWithBooks:
            raise Exception("Member has no book")
        if bookid not in self.borrowedBooks:
            raise Exception("Wrong book details")
        self.borrowedBooks.pop(bookid)
        self.membersWithBooks.remove(memid)

    def join(self, name, details):
        memberId = time.time()
        member = Member(memberId, name, details)
        self.members[memberId] = member
        return memberId

    def unsubscribe(self, memberId):
        if memberId not in self.members:
            raise Exception("Invalid Member")
        if memberId in self.membersWithBooks:
            raise Exception("Return the book first, buddy")
        return self.members.pop(memberId)

    def addBook(self, book):
        if book.bookid in self.books:
            raise Exception("Already added")
        self.books[book.bookid] = book
    
    def searchBook(bookId):
        return self.books[bookId]

class Book(object):
    def __init__(self, name, bid, author):
        self.name = name
        self.bookid = bid
        self.author = author

class Member(object):
    def __init__(self, name, mid):
        self.name = name
        self.memberid = mid
