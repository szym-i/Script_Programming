#!/bin/python3
from datetime import date
import argparse
import os


class Library:
    def __init__(self,content):
        self.lib = content
        self.users = {}

    def borrow(dane):
        pass

    def return_book(dane):
        pass

    def parseFileLine(linia):#przekształcenie linii pliku na struukturę danych
        self.lib[linia[0]] = linia[1] 

    def parseInputLine(linia):# przekształcenie linii standardowego wejścia na strukturę danych
        pass

def update(content):
    print("Welcome in my library, use Ctrl+D to stop")
    try:
        while True:
            inp = input()
            print(inp)
            content.append(inp)
    except EOFError:
        print(f"{content}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help = "enter library file", nargs=1)
    print(str(date.today()))
    print(repr(date.today()))
    print(str("Ala\n ma kota"))#nieformalna reprezentacja obiektu
    print(repr("Ala\n ma kota")) #formalna reprezentacja obiektu
    args = parser.parse_args()
    filename = args.file[0]
    try:
        if os.path.isfile(filename):
            file = open(filename,"r")
            print(f"File {filename} succesfully opened")
            content = file.readline().split()
            with open('somefile') as openfileobject:
                for line in openfileobject:
                    do_something()  
            file.close()
            update(content)
            #file = open(filename,"w")
            #file.write(''.join(content))
            #file.close()

        else:
            print(f"File {filename} does not exist")
    except PermissionError:
        print(f"No permission to open {filename}")
