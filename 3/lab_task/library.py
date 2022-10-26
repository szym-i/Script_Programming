#!/bin/python3

from datetime import date
import argparse
import os


class Library:
    def __init__(self,content):
        self.lib = content
        self.users = {}

    def __str__(self):
        return str(self.lib)+'\n'+str(self.users)

    def borrow(self,book,name):
        if book in self.lib.keys():
            if self.lib.get(book) > 0:
                print("Borrwing book...")
                self.lib[book] -=1
                if name not in self.users.keys():
                    self.users[name] = [book]
                elif name in self.users.keys():
                    self.users[name].append(book)
            else:
                print("Currently there are no copies of this book")
        else:
            print("There is not such book in our library")

    def return_book(self,book,name):
        if name not in self.users.keys() or book not in self.users[name]:
            print("You cannot return this book")
        else:
            print("Returning a book...")
            self.users[name].remove(book)

    def parseFileLine(self,linia):# przekształcenie linii pliku na struukturę danych
        self.lib[' '.join(linia[:-1])] = int(linia[-1])

    def parseInputLine(self,linia):# przekształcenie linii standardowego wejścia na strukturę danych
        pass

def update():
    print("Welcome in my library, use Ctrl+D to stop")
    while True:
        try:
            inp = input().split()
            operation = inp[0]
            book = ' '.join(inp[1:-1])
            name = inp[-1]
            if operation == "return":
                library.return_book(book,name)
            elif operation == "borrow":
                library.borrow(book,name)
            else:
                print("Use return/borrow operation")
        except EOFError:
            print(f"{library}")
            return
        except:
            print("Enter data as [operation] [book's title] [name]")
 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help = "enter library file", nargs=1)
    #print(str(date.today()))
    #print(repr(date.today()))
    #print(str("Ala\n ma kota"))#nieformalna reprezentacja obiektu
    #print(repr("Ala\n ma kota")) #formalna reprezentacja obiektu
    args = parser.parse_args()
    filename = args.file[0]
    try:
        if os.path.isfile(filename):
            with open(filename) as file:
                library = Library({})
                for line in file:
                    print(line.split())
                    library.parseFileLine(line.split())
            print(library)
            file.close()
            update()
            #file = open(filename,"w")
            #file.write(''.join(content))
            #file.close()
        else:
            print(f"File {filename} does not exist")
    except PermissionError:
        print(f"No permission to open {filename}")
