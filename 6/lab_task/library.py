#!/bin/python3

from datetime import date
from datetime import datetime
import argparse
import os
from reader import Person, Reader
from book import LibraryBook, ShopBook, BasicBook
import re
import warnings
import logging

def admin():
    print("Ta funkcja jest dla admina!")
    warnings.warn("you are not ADMIN!!")

def user(name):
    def inner(args):
        print(f"welcome {name}")
    return inner

class Library:

    def __init__(self,lb,rf="readers.txt",sb="shop_books.txt"):
        self.__library_books = []
        if lb != None:
            self.__library_books = self.read(lb,"lb")
        self.__readers = []
        if rf != None:
            self.__readers = self.read(rf,"r")
        self.lb = lb
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
    def revenue(self):
        return f"Total revenue: {ShopBook.revenue}$"

    @property
    def library_books(self):
        s = ""
        for e in self.__library_books:
            s+=str(e)+'\n'
        return s

    @property
    def shop_books(self):
        s=""
        for e in self.__shop_books:
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
        print("wywołano funkcje add")
        self.__readers.append(reader)

    def find_if_avaliable(self, title, authors, reader):
        for b in self.__library_books:
            if b.title == title and b.authors == authors and b.reader_pesel == '':
                reader + b
                return "The book has been borrowed!"
        return "No avaliable copies of this book to be borrowed"

    def is_borrowed_to_reader(self, bid, reader):
        if bid > len(self.__library_books)-1:
            return "There is no such book"
        return self.__library_books[bid].reader_pesel

    def save(self):
        f1 = open(self.lb,"w")
        for lb in self.__library_books:
            f1.write(lb.fileformat+'\n')
        f1.close()
        f2 = open(self.rf,"w")
        for r in self.__readers:
            f2.write(r.fileformat+'\n')
        f2.close()
        f3 = open(self.sb,"w")
        for sb in self.__shop_books:
            f3.write(sb.fileformat+'\n')
        f3.close()

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
            op = input("Enter operation (+/-/buy/add): ")
            if op == '-':
                bid = int(input("Enter book's ID="))
                if self.is_borrowed_to_reader(bid,reader) == reader.pesel:
                    reader - self.__library_books[bid]
                    return "The book was returned succesfully"
                else:
                    return "The book was not borrowed before, so you can't return it"
            if op == '+':
                title = input("Enter book's title:")
                authors = input("Enter book's authors(comma separated):")
                return self.find_if_avaliable(title, authors.split(','), reader)
            if op == 'buy':
                title = input("Enter book's title:")
                authors = input("Enter book's authors(comma separated):")
                return self.find_in_shop(title,authors.split(','),reader)
            if op == 'add':
                name = input("name:")
                surname = input("surname:")
                pesel = input("pesel:")
                self.add(Reader(name,surname,pesel))
            else:
                return "Enter valid operation"
    
    def find_in_shop(self, title, authors, reader):
        for sb in self.__shop_books:
            if sb.title == title and sb.authors == authors:
                if sb.quantity > 0:
                    reader + sb
                    return "Book has been bought"
                else:
                    return "No copies of this book for sale"
        return "No such book in our shop"

    def find_by_name(self,name):
        for r in self.__readers:
            if r.name == name:
                return r


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
    parser.add_argument('user', help = "enter name", nargs=1)
    args = parser.parse_args()
    filename = args.file[0]
    name = args.user[0]
    logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format=("%(asctime)s - %(levelname)s - %(message)s"))
    library = Library(filename)
    logging.info(f"{name} is logged")
    print(library)
    print(library.library_books)
    print(library.readers)
    print(library.shop_books)
    try:
        reader = library.find_by_name(name)
        if isinstance(reader, Reader):
            print(f"Welcome back {reader}")
        else:
            if name == 'ADMIN':
                print("Welcome ADMIN.")
            else:
                print("Contact ADMIN to create and account.")
                exit() 
        while True:
            print(library.parseInputLine(reader))
    except EOFError:
        print("End state")
        print(library.library_books)
        print(library.shop_books)
        print(library.revenue)
        library.save()
