from book import LibraryBook, ShopBook, BasicBook
from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, surname, pesel):
        self.__name = name
        self.__surname = surname
        self.__pesel = pesel

    def __str__(self):
        return f'{self.__name} {self.__surname}'

    def __repr__(self):
        return f'{self.__name} {self.__surname}' 

    def __eq__(self, other):
        if self.__name == other.name and self.__surname == other.surname and self.__pesel == other.pesel:
            return True
        return False
    
    @property
    def name(self):
        return self.__name
    
    @property
    def pesel(self):
        return self.__pesel
    
    @property
    def surname(self):
        return self.__surname
    

class Reader(Person):

    def __init__(self,name,surname,pesel):
        super().__init__(name,surname, pesel)

    @property
    def fileformat(self):
        return f'{self.name};{self.surname};{self.pesel}'

    def __add__(self, book: BasicBook):
        if isinstance(book, LibraryBook):
            book.reader_pesel = self.pesel
            book.borrow_date = datetime.now()
            book.history += f"PESEL:{self.pesel} {book.borrow_date}-"
            book.return_date = ''
        if isinstance(book, ShopBook):
            ShopBook.revenue += book.price
            book.quantity -= 1
            book.sold+=1


    def __sub__(self, book: LibraryBook):
        book.reader_pesel = ''
        book.return_date = datetime.now()
        book.history += f"{book.return_date}*"
        print(f"\033[93m Czas wypożyczenia: {book.return_date-book.borrow_date} \033[0m")
        book.borrow_date = ''
        return f'{self.name};{self.surname};{self.pesel}'



