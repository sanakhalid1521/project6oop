class Book:
    total_books = 0  # Class variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Adding books
book1 = Book()
book2 = Book()
Book.increment_book_count()  # Incrementing class variable

print(f"Total Books: {Book.total_books}")
