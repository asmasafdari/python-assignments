class Book:
    # Class variable
    total_books = 0
    # Class method
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
if __name__ == "__main__":
    # Incrementing the book count using the class method
    Book.increment_book_count()  # Output: Total books: 1
    Book.increment_book_count()  # Output: Total books: 2        
    Book.increment_book_count()  # Output: Total books: 3
    # Accessing the class variable
    
    print("Total books:", Book.total_books)  # Output: Total books: 2
    