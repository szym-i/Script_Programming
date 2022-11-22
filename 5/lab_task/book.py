from datetime import date
from datetime import datetime
from abc import ABC, abstractmethod

class BasicBook(ABC):
    number_of_books = 0
    def __init__(self, title: str, authors):
        self.__authors = authors.split(',')
        self.__title = title

    @property
    def title(self):
        return self.__title

    @property
    def authors(self):
        return self.__authors

    def __str__(self):
        return f'"{self.__title}" {",".join(map(str,self.__authors))}'

    def __repr__(self):
        return f'{self.__title} {",".join(map(str,self.__authors))}'

    def __eq__(self, other):
        if self.__title == other.title and self.__authors == other.authors and self.__borrow_date == other.borrow_date and self.__return_date == other.return_date:
            return True
        return False

class LibraryBook(BasicBook):

    n = 0
    def __init__(self,title,authors, borrow_date, return_date, reader_pesel, history):
        super().__init__(title,authors)
        self.__borrow_date = ''
        if borrow_date != '':
            self.__borrow_date = datetime.strptime(borrow_date,"%Y-%m-%d %H:%M:%S.%f")
        self.__return_date = ''
        if return_date != '':
            self.__return_date = datetime.strptime(return_date,"%Y-%m-%d %H:%M:%S.%f")
        self.__bid = LibraryBook.n
        LibraryBook.n += 1
        self.__reader_pesel = reader_pesel
        self.__history = history

    @property
    def fileformat(self):
        return f'{self.title};{",".join(map(str,self.authors))};{self.borrow_date};{self.return_date};{self.reader_pesel};{self.__history}'
    
    def __str__(self):
        return f'{str(self.bid)} "{self.title}" {",".join(map(str,self.authors))}\nHistory:{self.__history}'

    def __repr__(self):
        return f'{self.bid} {self.title} {",".join(map(str,self.authors))} {str(self.borrow_date)} {str(self.return_date)} {self.reader_pesel}'

    @property
    def bid(self):
        return self.__bid

    @property
    def reader_pesel(self):
        return self.__reader_pesel
    
    @reader_pesel.setter
    def reader_pesel(self,var):
        self.__reader_pesel = var

    @property
    def borrow_date(self):
        return self.__borrow_date

    @borrow_date.setter
    def borrow_date(self,var):
        self.__borrow_date = var

    @property
    def return_date(self):
        return self.__return_date

    @return_date.setter
    def return_date(self,var):
        self.__return_date = var

    @property
    def history(self):
        return self.__history

    @history.setter
    def history(self,var):
        self.__history = var

    def __del__(self):
        LibraryBook.n -= 1


class ShopBook(BasicBook):

    revenue = 0
    def __init__(self,title: str, authors, price: int, quantity: int):
        super().__init__(title,authors)
        if price > 0 and quantity >= 0:
            self.__price = price
            self.__quantity = quantity
            self.__sold = 0
        else:
            raise ValueError("Price need to be > 0 and quantity >= 0!")

    def __str__(self):
        return f'"{self.title}" {",".join(map(str,self.authors))}\nRevenue:{self.__price}$ Sold:{self.__sold}'

    def buy(self):
        if self.__quantity > 0:
            ShopBook.revenue += self.__price
            self.__quantity -= 1
            self.__sold+=1
            return "The book has been bought"
        return "Cannot buy this book"
