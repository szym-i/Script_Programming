#!/bin/python3

from datetime import date
import argparse
import os


class Library:
    def __init__(self):
        self.lib = {}
        self.usr = {}

    def __str__(self):
        return str(self.lib)+'\n'+str(self.usr)

    def borrow(self,book,name):
        if book in self.lib.keys():
            if self.lib.get(book) > 0:
                print("Borrwing book...")
                self.lib[book] -=1
                if name not in self.usr.keys():
                    self.usr[name] = [book]
                elif name in self.usr.keys():
                    self.usr[name].append(book)
            else:
                print("Currently there are no copies of this book")
        else:
            print("There is not such book in our library")

    def return_book(self,book,name):
        if name not in self.usr.keys() or book not in self.usr[name]:
            print("You cannot return this book")
        else:
            print("Returning a book...")
            self.usr[name].remove(book)
            self.lib[book] +=1

    def parseFileLine(self,line):# przekształcenie linii pliku na struukturę danych
        key, value = line.strip().split(':')
        self.lib[key] = int(value)

    def parseInputLine(self,line):# przekształcenie linii standardowego wejścia na strukturę danych
        if len(line) < 3:
            print("[operation] [book's title] [name]")
            return
        op = line[0]
        title = ' '.join(line[1:-1])
        name = line[-1]
        if op == "return":
            library.return_book(title,name)
        elif op == "borrow":
            library.borrow(title,name)
        else:
            print("Use return/borrow operation")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help = "enter library file", nargs=1)
    #print(str(date.today()))
    #print(repr(date.today()))
    #print(str("Ala\n ma kota"))#nieformalna reprezentacja obiektu
    #print(repr("Ala\n ma kota")) #formalna reprezentacja obiektu
    args = parser.parse_args()
    filename = args.file[0]
    library = Library()
    try:
        if os.path.isfile(filename):
            with open(filename) as file:
                for line in file:
                    library.parseFileLine(line)
            file.close()
        else:
            print(f"File {filename} does not exist")
    except PermissionError:
        print(f"No permission to open {filename}")
    print(f"{library}")
    print("Welcome in my library, use Ctrl+D to stop")
    try:
        while True:
            line = input().split()
            library.parseInputLine(line)
    except:
        print("End state")
        file = open(filename,"w")
        for k,v in library.lib.items():
            file.write(f"{k}: {v}\n")
        file.close()
        print(library)
