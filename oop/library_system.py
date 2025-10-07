class Book:
    """
    Base class representing a general book.
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        """Returns the user-friendly string representation (details) of the book."""
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

    def __str__(self):
        """Returns the string representation specific to an EBook."""
        # Use the base class __str__ and append the unique attribute
        # Note: We replace "Book: " with "EBook: " for accurate output
        base_details = super().__str__().replace("Book: ", "EBook: ")
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

    def __str__(self):
        """Returns the string representation specific to a PrintBook."""
        # Use the base class __str__ and append the unique attribute
        # Note: We replace "Book: " with "PrintBook: " for accurate output
        base_details = super().__str__().replace("Book: ", "PrintBook: ")
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
        """Prints the details of each book in the library using the __str__ method."""
        for book in self.books:
            # When we print the book object, Python automatically calls the __str__ method (Polymorphism)
            print(book)