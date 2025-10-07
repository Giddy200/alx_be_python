class Book:
    """
    Base class representing a general book.
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self):
        """Returns the basic details of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds file_size.
    """
    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        """Returns the details specific to an EBook."""
        # Use details from the base class and add the unique attribute
        base_details = super().get_details().replace("Book: ", "EBook: ")
        return f"{base_details}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a physical print book.
    Inherits from Book and adds page_count.
    """
    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        """Returns the details specific to a PrintBook."""
        # Use details from the base class and add the unique attribute
        base_details = super().get_details().replace("Book: ", "PrintBook: ")
        return f"{base_details}, Page Count: {self.page_count}"

class Library:
    """
    Class demonstrating composition, managing a collection of book objects.
    """
    def __init__(self):
        # The 'books' attribute is a list composed of Book/EBook/PrintBook instances
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library collection."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Item is not a valid book instance.")

    def list_books(self):
        """Prints the details of each book in the library using polymorphism."""
        for book in self.books:
            # Polymorphism in action: calling .get_details() on any type 
            # of book instance calls the specific implementation (Book, EBook, or PrintBook).
            print(book.get_details())