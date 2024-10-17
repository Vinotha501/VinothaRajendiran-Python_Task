# Design a Library Management System

class Book:
    def __init__(self, title, author, publication_date, copies):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.copies = copies
        self.borrow_day = None

    def available(self):
        return self.copies > 0

    # Borrowed books
    def Borrow(self, member, current_day):
        if self.copies > 0:
            self.copies -= 1
            self.borrow_day = current_day
            print(f"Borrowed : {self.title}")
        else:
            print(f"{self.title} is unavailable")
            member.notify_book_availability(self)

    # Returned books   
    def Return(self):
        self.copies += 1
        print(f"Returned : {self.title}")

    # fine calculation
    def calculate_fine (self, current_day):
        if self.borrow_day is not None and (current_day - self.borrow_day) > 5:
            days_overdue = (current_day - self.borrow_day) - 5
            fine = days_overdue
            return fine
        return 0


class Librarycard:
    def __init__(self, member_name):
        self.member_name = member_name
        self.borrowing_history = []

    def add_borrow_record(self, book):
        self.borrowing_history.append(f"Borrowed : '{book.title}'")
    

    def add_return_record(self, book):
        self.borrowing_history.append(f"Returned : '{book.title}'")
       

    def show_history(self):
        print (f"Library Card for {self.member_name}")
        if self.borrowing_history:
            print ("Borrowing history:")
            for record in self.borrowing_history:
                print (record)
        else:
            print ("No borrowing history.")


class Member:
    def __init__(self, Name, E_mail, Phone_number):
        self.Name = Name
        self.E_mail = E_mail
        self.Phone_number = Phone_number
        self.borrowed_books = []
        self.library_card = Librarycard(self.Name)


    # Borrowed books
    def Borrow_book(self, book, current_day):
        if book.available():
            book.Borrow(self, current_day)
            self.borrowed_books.append(book)
            self.library_card.add_borrow_record(book)
        else:
            print(f"'{book.title}' is not available")
            self.notify_book_availability(book)


    # Returned book
    def Return_book(self, book, current_day):
        if book in self.borrowed_books:
            fine = book.calculate_fine(current_day)
            if fine > 0:
                print(f"Fine : You have a fine of Rs.{fine} for returning '{book.title}' late.")
            book.Return()
            self.borrowed_books.remove(book)
            self.library_card.add_return_record(book)
        else:
            print(f"You haven't borrowed the book {book.title}")


    def notify_book_availability(self, book):
        print (f"Notification: '{book.title}' will be available soon. You will be notified when it is ready.")


class Librarian:
    def __init__(self, Name, Id):
        self.Name = Name
        self.Id = Id

    def add_books (self, library, book):
        library.books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library")


    def remove_books(self, library, book_title):
        for book in library.books:
            if book.title == book_title:
                library.books.remove(book)
                print (f"Removed '{book_title}' from the library.")
                return
        print (f"Book '{book_title}' not found in the library")


    def update_copies(self,library, book_title, new_copies):
        for book in library.books:
            if book.title == book_title:
                book.copies = new_copies
                print (f"Updated '{book.title}' to {new_copies} copies.")
                return
        print (f"Book '{book_title}' not found in the library.")


class Library:
    def __init__(self, Name):
        self.Name = Name
        self.books = []

    # Searching a book
    def search_book(self, query):
        query = query.lower() 
        result = []
        for book in self.books:
            if query in book.title.lower()or query in book.author.lower():
                result.append(book)

        if result:
            print(f"Search results for '{query}':")
            for book in result:
                print(f"'{book.title}' by {book.author} - {book.copies} copies available")
        else:
            print(f"No results found for '{query}'")

    def list_books(self):
        for book in self.books:
            print(f"'{book.title}' - {book.copies} copies available")


# Create a library 
library = Library("Global Library")

# Books
book1 = Book("House of Fame", "Virginia Woolf", 1890, 5)
book2 = Book("Canterbury Tales", "Chaucer", 1780, 4)
book3 = Book("Dr.Fastus", "Christopher", 1880, 4)
book4 = Book ("Sonnet", "Shakespeare", 1770,0)

# Librarian 
librarian = Librarian("John", "A2003")

# Add books to the library
print("\nBooks added to the library:")
librarian.add_books(library, book1)
librarian.add_books(library, book2)
librarian.add_books(library, book3)

# Member 
member1 = Member("Shelly", "shelly@example.com", "973-456-7890")
member2 = Member("Byron", "byron@example.com", "903-797-9890")

# borrowing days count
print ("\nCalculating the fine : ")
current_day = 1  
member1.Borrow_book(book1, current_day) 

# overdue
current_day += 15
member1.Return_book(book1, current_day)

# Trying to borrow an unavailable book
print("\nTrying to borrow an unavailable book:")
member1.Borrow_book(book4, current_day)

# borrowing history of members
print ("\nLibrary card details:")
member1.library_card.show_history()

# Searching for a book
print("\nSearching for a book:")
library.search_book ("Virginia Woolf")
library.search_book ("Canterbury Tales")
library.search_book ("Henry V11")

#list of books after adding
print("\nBefore updating books:")
library.list_books()

# updated copies
print("\nUpdated copies:")
librarian.update_copies(library,"Dr.Fastus",2)

#list updated copies
print("\nAfter updating books:")
library.list_books()

# remove a book
print("\nRemoving a book:")
librarian.remove_books(library, "House of Fame" )

# List of books after removal
print("\nAfter removing a book:")
library.list_books()

# List of books in the library
print("\nList of Books:")
library.list_books()
print("\n")
