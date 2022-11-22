from book import LibraryBook, ShopBook
from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, surname, pesel, history="Pusta historia"):
        self.__name = name
        self.__surname = surname
        self.__pesel = pesel
        self.__history = history

    def __str__(self):
        return f'{self.__name} {self.__surname}'

    def __repr__(self):
        return f'{self.__name} {self.__surname}' 

    def __eq__(self, other):
        if self.__name == other.name and self.__surname == other.surname:
            return True
        return False
    
    @abstractmethod
    def welcome(self):
        pass
    
    @property
    def name(self):
        return self.__name
    
    @property
    def pesel(self):
        return self.__pesel
    
    
    #@name.setter
    #def name(self,var):
     #   self.__name = var

    @property
    def surname(self):
        return self.__surname
    

class Reader(Person):

    def __init__(self,name,surname,pesel):
        super().__init__(name,surname, pesel)

    def __add__(self, book: LibraryBook):
        book.reader_pesel = self.pesel
        book.borrow_date = datetime.now()
        book.history += f"PESEL:{self.pesel} {book.borrow_date}-"
        book.return_date = ''

    def __sub__(self, book: LibraryBook):
        book.reader_pesel = ''
        book.return_date = datetime.now()
        book.history += f"{book.return_date} Czas wypożyczenia:{book.return_date-book.borrow_date}\n"
        print(f"\033[93m Czas wypożyczenia: {book.return_date-book.borrow_date} \033[0m")
        book.borrow_date = ''

    @property
    def fileformat(self):
        return f'{self.name};{self.surname};{self.pesel}'

    def welcome(self):
        print("Welcome reader!")

class Shopper(Person):

    def __add__(self, book: ShopBook):
        if book.quantity > 0:
            ShopBook.revenue += book.price
            book.quantity -= 1
            book.sold+=1
            return "The book has been bought"
        return "Cannot buy this book"

    def welcome(self):
        print("Welcome shopper!")


if __name__=='__main__':
    shopper = Shopper("imie","nazwisko","123")
    shopper.welcome()
    book = ShopBook('title','author',2,3)
    book2 = ShopBook('title2','author2',10,1)
    shopper+book
    shopper+book2
    shopper+book
    shopper+book
    shopper+book
    print(ShopBook.revenue)
