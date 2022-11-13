#!/bin/python3

from datetime import date
from datetime import datetime
import argparse
import os
from reader import Reader
from book import Book
import re

class Library:
    def __init__(self,bf,rf="readers.txt"):
        self.__books = []
        if bf != None:
            self.__books = self.read(bf,"books")
        self.__readers = []
        if rf != None:
            self.__readers = self.read(rf,"readers")
        self.bf = bf
        self.rf = rf

    def __str__(self):
        s="     TITLE:              BORROW_DATE:            READER:\n"
        for b in self.__books:
            if b.reader_pesel != '':
                r = self.find_reader(b.reader_pesel)
                s += f'{b.title:^16} {str(b.borrow_date):^20} {r.name:^14} {r.surname:^20}'
        return s

    @property
    def pesele(self):
        return [e.pesel for e in self.__readers ]

    @property
    def books(self):
        s="BID:        TITLE:                AUTHORS:                   BORROW_DATE:                RETURN_DATE:            READER_PESEL:\n"
        for b in self.__books:
            s+=repr(b)+'\n'
        return s

    @property
    def readers(self):
        s = " NAME:               SURNAME:          PESEL:\n"
        for r in self.__readers:
            s+=repr(r)+'\n'
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
        for b in self.__books:
            f1.write(b.fileformat+'\n')
        f1.close()
        f2 = open(self.rf,"w")
        for r in self.__readers:
            f2.write(r.fileformat+'\n')
        f2.close()

    def parseFileLine(self,line, op):# przekształcenie linii pliku na strukturę danych
        print(line)
        args = line.strip().split(';')
        if op == "books":
            try:
                return Book(*args)
            except:
                print("Converting books file line file went wrong")
        if op == "readers":
            try:
                return Reader(*args)
            except:
                print("Converting readers file line went wrong")

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
    print(library.books)
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
        print(reader)
        if reader in library.readers_list:
            print(f"Welcome back {reader.name}")
        else:
            if pesel in library.pesele:
                print("Podszywasz się pod kogoś lub wprowadziłeś niepoprawne dane")
                exit() 
            else:
                print("Creating reader profile for new user...")
                library.add(reader)
        while True:
            print(library.parseInputLine(reader))
    except EOFError:
        print("End state")
        #print(library)
        library.save()
