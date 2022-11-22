from book import LibraryBook, ShopBook
from datetime import datetime, timedelta

class Person:

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def __str__(self):
        return f'{self.__name} {self.__surname}'

    def __repr__(self):
        return f'{self.__name} {self.__surname}' 

    def __eq__(self, other):
        if self.__name == other.name and self.__surname == other.surname:
            return True
        return False

    @property
    def name(self):
        return self.__name
    
    #@name.setter
    #def name(self,var):
     #   self.__name = var

    @property
    def surname(self):
        return self.__surname
    

class Reader(Person):

    def __init__(self,name,surname,pesel):
        super().__init__(name,surname)
        self.__pesel = pesel

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

    @property
    def pesel(self):
        return self.__pesel
    
    @pesel.setter
    def pesel(self,var):
        self.__pesel = var


class Shopper(Person):
    pass

if __name__=='__main__':
    reader = Reader("imie","nazwisko","123")
    print(reader)
