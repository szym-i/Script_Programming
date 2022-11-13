from book import Book
from datetime import datetime, timedelta

class Reader:

    def __init__(self, name, surname, pesel):
        self.__name = name
        self.__surname = surname
        self.__pesel = pesel

    def __str__(self):
        return f'{self.__name} {self.__surname}'

    def __repr__(self):
        return f'{self.__name:14} {self.__surname:^20} {self.__pesel:^11}' 

    def __eq__(self, other):
        if self.__name == other.name and self.__surname == other.surname and self.__pesel==other.pesel:
            return True
        return False

    def __add__(self, book: Book):
        book.reader_pesel = self.pesel
        book.borrow_date = datetime.now()
        book.return_date = ''

    def __sub__(self, book: Book):
        book.reader_pesel = ''
        book.return_date = datetime.now()
        print(f"Czas wypożyczenia: {book.return_date-book.borrow_date}")
        book.borrow_date = ''

    @property
    def fileformat(self):
        return f'{self.__name};{self.surname};{self.pesel}'

    @property
    def pesel(self):
        return self.__pesel
    
    @pesel.setter
    def pesel(self,var):
        self.__pesel = var

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,var):
        self.__name = var

    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self,var):
        self.__surname = var


