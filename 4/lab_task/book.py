from datetime import date
from datetime import datetime

class Book:

    number_of_books = 0
    def __init__(self, title, authors, borrow_date, return_date, reader_pesel):
        self.__authors = authors.split(',')
        self.__title = title
        self.__borrow_date = ''
        if borrow_date != '':
            self.__borrow_date = datetime.strptime(borrow_date,"%Y-%m-%d %H:%M:%S.%f")
        self.__return_date = ''
        if return_date != '':
            self.__return_date = datetime.strptime(return_date,"%Y-%m-%d %H:%M:%S.%f")
        self.__bid = Book.number_of_books
        Book.number_of_books+=1
        self.__reader_pesel = reader_pesel

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
    def title(self):
        return self.__title

    @property
    def authors(self):
        return self.__authors

    @property
    def fileformat(self):
        return f'{self.title};{",".join(map(str,self.__authors))};{self.borrow_date};{self.return_date};{self.reader_pesel}'
    
    def __str__(self):
        return f'{str(self.__bid)} "{self.__title}" {",".join(map(str,self.__authors))}'

    def __repr__(self):
        return f'{self.__bid:^3} {self.__title:^20} {",".join(map(str,self.__authors)):^25} {str(self.__borrow_date):^30} {str(self.__return_date):^30} {self.__reader_pesel:^11}'

if __name__ == '__main__':
    args = "1984;George Orwell;2022-11-13 14:45:31.261705;;1".split(';')
    print(args)
    book1 = Book(*args)
    print(repr(book1))
    #dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #print(dt_string)
