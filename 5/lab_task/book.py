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
        hs = "\n".join(self.__history.split("*"))
        return f'{str(self.bid)} "{self.title}" {",".join(map(str,self.authors))}\nHistory:\n{hs}'

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
    def __init__(self,title: str, authors, price: int, quantity: int, sold: int):
        super().__init__(title,authors)
        if int(price) > 0 and int(quantity) >= 0:
            self.__price = int(price)
            self.__quantity = int(quantity)
            self.__sold = int(sold)
            ShopBook.revenue += self.__sold*self.__price
        else:
            raise ValueError("Price need to be > 0 and quantity >= 0!")

    def __str__(self):
        return f'"{self.title}" {",".join(map(str,self.authors))}\nQuantity:{self.quantity}\nPrice:{self.__price}$ Sold:{self.__sold}\nRevenue from this book:{self.__sold*self.__price}$'

    @property
    def price(self):
        return self.__price

    @property
    def fileformat(self):
        return f'{self.title};{",".join(map(str,self.authors))};{self.price};{self.quantity};{self.sold}'

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self,var):
        self.__quantity = var

    @property
    def sold(self):
        return self.__sold

    @sold.setter
    def sold(self,var):
        self.__sold = var
