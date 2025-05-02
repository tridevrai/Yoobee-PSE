# Activity1 : Deadline 2 May - Library Book Manager Using classes
# Task: Manage a small library — add and show books.

# 1. Create a class Book with the following attributes:
# - title
# - author
# - isbn
# - status (available, borrowed)


#2 create a class Library with the following attributes:
# - books
# - add book
# - remove book
# - show all books
# - borrow book
# - return book
# - show all borrowed books
# - show all available books


class Book:
    #constructor
    def __init__(self):
        self.title = ""
        
    def build_book(self,book_info):
        book_info = book_info.split(",")
        self.title = book_info[0].strip()   
        self.author = book_info[1].strip()
        self.isbn = book_info[2].strip()
        self.status = book_info[3].strip()
        return self
        
    def show_book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status}")
    
    def borrow_book(self):
        self.status = "borrowed"
        
    def return_book(self):
        self.status = "available"

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self):
        while True:
            book_info = input("Enter the book information as comma separated values (title, author, isbn, status): ")
            if book_info.count(",") != 3:
                print("Invalid book information\n")
                self.add_book()
            else:
                break
        book = Book().build_book(book_info)
        self.books.append(book)
        
    def remove_book(self,isbn_to_remove):
        for book in self.books:
            if book.isbn == isbn_to_remove:
                self.books.remove(book)
                print(f"Book with ISBN {isbn_to_remove} removed successfully")
                return
        print(f"Book with ISBN {isbn_to_remove} not found")
        
    def show_all_books(self):
        for book in self.books:
            book.show_book_info()
        
    def show_all_borrowed_books(self):
        for book in self.books:
            if book.status.strip() == "borrowed":
                book.show_book_info()
                
    def show_all_available_books(self):
        for book in self.books:
            if book.status.strip() == "available":
                book.show_book_info()
                
    def borrow_book(self,isbn_to_borrow):
        for book in self.books:
            if book.isbn == isbn_to_borrow:
                book.borrow_book()
                return
        print(f"Book with ISBN {isbn_to_borrow} not found")
        
    def return_book(self,isbn_to_return):
        for book in self.books:
            if book.isbn == isbn_to_return:
                book.return_book()
                return
        print(f"Book with ISBN {isbn_to_return} not found")
    
    def menu(self):
        while True:
            print("1. Add book")
            print("2. Remove book")
            print("3. Show all books")
            print("4. Show all borrowed books")
            print("5. Show all available books")    
            print("6. Borrow book")
            print("7. Return book")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_book() 
            elif choice == "2":
                isbn_to_remove = input("Enter the ISBN of the book to remove: ")
                self.remove_book(isbn_to_remove)
            elif choice == "3":
                self.show_all_books()
            elif choice == "4":
                self.show_all_borrowed_books()  
            elif choice == "5":
                self.show_all_available_books()
            elif choice == "6":
                isbn_to_borrow = input("Enter the ISBN of the book to borrow: ")
                self.borrow_book(isbn_to_borrow)
            elif choice == "7":
                isbn_to_return = input("Enter the ISBN of the book to return: ")
                self.return_book(isbn_to_return)
            elif choice == "8":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice\n")

library = Library()
library.menu()














