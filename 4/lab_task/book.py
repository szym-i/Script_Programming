from datetime import date

class Book:

    number_of_books = 0
    def __init__(self, authors, title, borrow_date=None, return_date=None):
        self.__reader_pesel = None
        self.__authors = authors
        self.__title = title
        self.__borrow_date = borrow_date
        self.__return_date = return_date
        self.__bid = Book.number_of_books
        Book.number_of_books+=1

    @reader_pesel
    def reader_pesel(self):
        return self.__reader_pesel

    @setter.reader_pesel
    def reader_pesel(self,var):
        self.__reader_pesel = var

    def __str__(self):
        return f'"{self.__title}" {self.__authors} {self.__bid}'

    def __repr__(self):
        return f'"{self.__title}" {self.__authors}'

if __name__ == '__main__':
    book1 = Book(["Author11","Author12"],"book1","","")
    book2 = Book("Author","book2","","")
    print(book1)
    print(book1.reader_pesel)
