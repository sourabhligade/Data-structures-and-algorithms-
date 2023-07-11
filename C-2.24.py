#Suppose you are on the design team for a new e-book reader. What are the primary classes and
#methods that the Python software for your reader will need? You should include an inheritance 
#diagram for this code, but you do not need to write any actual code. 
#Your software architecture should at least include ways for customers to buy new books, 
#view their list of purchased books, and read their purchased books.





class EBookReader:
    def __init__(self):
        self.purchased_books = []

    def buy_book(self, book):
        self.purchased_books.append(book)
        print(f"Book '{book.get_title()}' purchased successfully.")

    def view_purchased_books(self):
        print("Purchased Books:")
        for book in self.purchased_books:
            print(f"- {book.get_title()} by {book.get_author()}")

    def read_book(self, book):
        print(f"Reading '{book.get_title()}'...")
        content = book.get_content()
        print(content)


class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_content(self):
        return self.content


reader = EBookReader()

book1 = Book("Python Programming", "John Smith", "Contents of the Python programming book.")

reader.buy_book(book1)
reader.view_purchased_books()

selected_book = reader.purchased_books[0]
reader.read_book(selected_book)
