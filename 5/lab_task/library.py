#!/bin/python3

from datetime import date
from datetime import datetime
import argparse
import os
from reader import Person, Reader, Shopper
from book import LibraryBook, ShopBook, BasicBook
import re

class Library:

    def __init__(self,bf,rf="readers.txt",sb="shop_books.txt"):
        self.__library_books = []
        if bf != None:
            self.__library_books = self.read(bf,"lb")
        self.__readers = []
        if rf != None:
            self.__readers = self.read(rf,"r")
        self.bf = bf
        self.rf = rf
        self.__shop_books = []
        if sb != None:
            self.__shop_books = self.read(sb,"sb")
        self.sb = sb

    def __str__(self):
        s="     TITLE:              BORROW_DATE:            READER:\n"
        for b in self.__library_books:
            if b.reader_pesel != '':
                r = self.find_reader(b.reader_pesel)
                s += f'{b.title:^16} {str(b.borrow_date):^20} {r.name:^14} {r.surname:^20}\n'
        return s

    @property
    def pesele(self):
        return [e.pesel for e in self.__readers ]

    #@property
    #def books(self):
    #    s="BID:        TITLE:                AUTHORS:                   BORROW_DATE:                RETURN_DATE:            READER_PESEL:\n"
    #    for b in self.__books:
    #        s+=f'{b.bid:^3} {b.title:^20} {",".join(map(str,b.authors)):^25} {str(b.borrow_date):^30} {str(b.return_date):^30} {b.reader_pesel:^11}\n'
    #    return s
    
    @property
    def library_books(self):
        s = ""
        for e in self.__library_books:
            s+=str(e)+'\n'
        return s

    @property
    def readers(self):
        s = " NAME:               SURNAME:          PESEL:\n"
        for r in self.__readers:
            s+=f'{r.name:14} {r.surname:^20} {r.pesel:^11}\n'
        return s

    @property
    def readers_list(self):
        return self.__readers

    def find_reader(self,reader_pesel):
        for r in self.__readers:
            if r.pesel == reader_pesel:
                return r
        return "An error occured"

    def add(self,reader):
        self.__readers.append(reader)

    def find_if_avaliable(self, title, authors, reader):
        for b in self.__books:
            if b.title == title and b.authors == authors and b.reader_pesel == '':
                reader + b
                return "The book has been borrowed!"
        return "No avaliable copies of this book to be borrowed"

    def is_borrowed_to_reader(self, bid, reader):
        if bid > len(self.__books)-1:
            return "There is no such book"
        return self.__books[bid].reader_pesel

    def save(self):
        f1 = open(self.bf,"w")
        for b in self.__library_books:
            f1.write(b.fileformat+'\n')
        f1.close()
        f2 = open(self.rf,"w")
        for r in self.__readers:
            f2.write(r.fileformat+'\n')
        f2.close()

    def parseFileLine(self,line, op):# przekształcenie linii pliku na strukturę danych
        args = line.strip().split(';')
        if op == "lb":
            try:
                return LibraryBook(*args)
            except:
                print("Converting library books file line file went wrong")
        if op == "r":
            try:
                return Reader(*args)
            except:
                print("Converting readers file line went wrong")
        if op == "sb":
            try:
                return ShopBook(*args)
            except:
                print("Converting shop books file line file went wrong")

    def parseInputLine(self,reader):# przekształcenie linii standardowego wejścia na strukturę danych
            op = input("Enter operation (+/-): ")
            if op == '-':
                bid = int(input("Enter book's ID="))
                if self.is_borrowed_to_reader(bid,reader) == reader.pesel:
                    reader - self.__books[bid]
                    return "The book was returned succesfully"
                else:
                    return "The book was not borrowed before, so you can't return it"
            if op == '+':
                title = input("Enter book's title:")
                authors = input("Enter book's authors(comma separated):")
                print(self.find_if_avaliable(title, authors.split(','), reader))
            else:
                return "Enter valid operation"
    
    @staticmethod
    def welcome(reader):
        print(reader.welcome)
    
    @staticmethod
    def check_filename(filename):
        if os.path.isfile(filename):
            try:
                file = open(filename)
                return file
            except PermissionError:
                return f"No permission to open file"
        return "No such file exists"

    def read(self,filename,op):
        list = []
        file = self.check_filename(filename)
        if file != "No permission to open file" and file != "No such file exists":
            for line in file:
                x=self.parseFileLine(line,op)
                if not isinstance(x, type(None)):
                    list.append(x)
            file.close()
        else:
            print(file)
        return list

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help = "enter library file", nargs=1)
    args = parser.parse_args()
    filename = args.file[0]
    library = Library(filename)
    print(library)
    print(library.library_books)
    print(library.readers)
    print("Welcome in my library, use Ctrl+D to stop")
    try:
        name = input("Enter your name:").strip()
        surname = input("Enter your surname:").strip()
        pesel_pattern = re.compile(r'^\d{11}$')#11
        pesel = "00"
        while not pesel_pattern.match(pesel):
            pesel = input("Enter your pesel (11-digits):").strip()
        reader = Reader(name,surname,pesel)
        if reader in library.readers_list:
            print(f"Welcome back {reader}")
            library.welcome(reader)
        else:
            if pesel in library.pesele:
                print("Podszywasz się pod kogoś lub wprowadziłeś niepoprawne dane")
                exit() 
            else:
                print("Creating reader profile for {reader}")
                library.add(reader)
        while True:
            print(library.parseInputLine(reader))
    except EOFError:
        print("End state")
        print(library.library_books)
        library.save()
