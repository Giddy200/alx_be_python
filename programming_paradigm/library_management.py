# library_management.py

class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a Book instance.
        
        :param title: The title of the book (public).
        :param author: The author of the book (public).
        """
        self.title = title
        self.author = author
        # Private attribute to track checkout status
        self._is_checked_out = False 

    def check_out(self):
        """Marks the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False # Already checked out

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False # Already available

    def is_available(self):
        """Returns True if the book is not checked out, False otherwise."""
        return not self._is_checked_out
    
    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects and handles check-out/return operations.
    """
    def __init__(self):
        # Private list to store Book instances
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book objects can be added to the library.")

    def _find_book(self, title):
        """Helper method to find a book by its title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        """
        Attempts to check out a book by title.
        :param title: The title of the book to check out.
        """
        book = self._find_book(title)
        if book:
            if book.check_out():
                print(f"'{title}' successfully checked out.")
            else:
                print(f"'{title}' is already checked out.")
        else:
            print(f"Book with title '{title}' not found.")

    def return_book(self, title):
        """
        Attempts to return a book by title.
        :param title: The title of the book to return.
        """
        book = self._find_book(title)
        if book:
            if book.return_book():
                print(f"'{title}' successfully returned.")
            else:
                print(f"'{title}' was not checked out.")
        else:
            print(f"Book with title '{title}' not found.")

    def list_available_books(self):
        """Prints the title and author of all books that are currently available."""
        available_books_count = 0
        for book in self._books:
            if book.is_available():
                print(book)
                available_books_count += 1
        
        if available_books_count == 0:
            print("No books are currently available.")