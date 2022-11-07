#!/bin/python3

from datetime import date
import argparse
import os

def read_usr(filename):
    d = {}
    with open(filename,"r") as f:
        try:
            for line in f:
                k, l = line.strip().split(':')
                l = l[1:-1]
                res = l.strip('][').split(', ')
                for i in range(0,len(res)):
                    res[i] = res[i][1:-1]
                d[k] = res
        except:
            print(f"Oops, reading {filename} file went wrong")
            return {}
    f.close()
    return d


class Library:
    def __init__(self,filename,filename2="usr.txt"):
        self.lib = {}
        try:
            if os.path.isfile(filename):
                with open(filename) as file:
                    for line in file:
                        self.parseFileLine(line)
                file.close()
            else:
                print(f"File {filename} does not exist")
        except PermissionError:
            print(f"No permission to open {filename}")
        self.usr = read_usr(filename2)
        self.filename2 = filename2

    def __str__(self):
        s = ""
        for k,v in self.lib.items():
            s+=k+':'+str(v)+"\n"
        for k,v in self.usr.items():
            s+=k+':'+str(v)+'\n'
        return s

    def borrow(self,book,name):
        if book in self.lib.keys():
            if self.lib.get(book) > 0:
                self.lib[book] -=1
                if name not in self.usr.keys():
                    self.usr[name] = [book]
                elif name in self.usr.keys():
                    self.usr[name].append(book)
                return "The book has been borrowed"
            else:
                return "Currently there are no copies of this book"
        else:
            return "There is not such book in our library"

    def return_book(self,book,name):
        if name not in self.usr.keys() or book not in self.usr[name]:
            return "You cannot return this book"
        else:
            self.usr[name].remove(book)
            self.lib[book] +=1
            return "The book has been returned"

    def parseFileLine(self,line):# przekształcenie linii pliku na struukturę danych
        key, value = line.strip().split(':')
        self.lib[key] = int(value)

    def parseInputLine(self,line):# przekształcenie linii standardowego wejścia na strukturę danych
        line = line.split()
        if len(line) < 3:
            print("[operation] [book's title] [name]")
            return
        op = line[0]
        title = ' '.join(line[1:-1])
        name = line[-1]
        if op == "return":
            return self.return_book(title,name)
        elif op == "borrow":
            return self.borrow(title,name)
        else:
            return "Use return/borrow operation"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help = "enter library file", nargs=1)
    #print(str(date.today()))
    #print(repr(date.today()))
    #print(str("Ala\n ma kota"))#nieformalna reprezentacja obiektu
    #print(repr("Ala\n ma kota")) #formalna reprezentacja obiektu
    args = parser.parse_args()
    filename = args.file[0]
    library = Library(filename)
    print(f"{library}")
    print("Welcome in my library, use Ctrl+D to stop")
    try:
        while True:
            line = input()
            print(library.parseInputLine(line))
    except:
        print("End state")
        file = open(filename,"w")
        for k,v in library.lib.items():
            file.write(f"{k}:{v}\n")
        file.close()
        with open(library.filename2,"w") as f:
            for k,v in library.usr.items():
                f.write(f"{k}:{v}\n")
        print(library)
