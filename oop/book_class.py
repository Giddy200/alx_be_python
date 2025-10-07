class Book:
    """
    A class to represent a book, utilizing Python's magic methods 
    for initialization, representation, and cleanup.
    """
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor: Initializes a new Book instance.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book created: {self.title}") # Optional: Confirmation of creation

    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed/deleted.
        """
        # This print statement is the requirement for the __del__ method
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation: Returns a user-friendly string for the book.
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Returns a string that can be used to recreate 
        the object.
        Format: f"Book('{self.title}', '{self.author}', {self.year})"
        """
        # Note the use of quotes around string attributes (title and author)
        # to ensure the output string is valid Python code.
        return f"Book('{self.title}', '{self.author}', {self.year})"

# End of book_class.py