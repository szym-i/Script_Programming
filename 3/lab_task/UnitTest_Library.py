import unittest
from library import Library

library1 = Library("tests/test1.txt")
library2 = Library("tests/test2.txt")

class Test_Library(unittest.TestCase):
    def test__str__(self):
        self.assertEqual(str(library1), "1984:2\nGwiezdne Wojny:2\nSzymon:['']\nAla:['']\nTomek:['']\n")
        self.assertEqual(str(library2), "Duma i uprzedzenie:2\nWładca Pierścieni:0\nZabić drozdad:31\nBiblia:1\nWichrowe Wzgórza:0\nRok 1984:1984\nWielkie nadzieje:1\nSzymon:['']\nAla:['']\nTomek:['']\n")

    def test_borrow(self):
        self.assertEqual(library1.borrow("1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library1.borrow("1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library1.borrow("1984","Szymon"), "Currently there are no copies of this book")
        self.assertEqual(library1.borrow("1984","Ala"), "Currently there are no copies of this book")
        self.assertEqual(library1.borrow("1984","Tomek"), "Currently there are no copies of this book")
        self.assertEqual(library1.borrow("Gwiezdne Wojny","Tomek"), "The book has been borrowed")
        self.assertEqual(library1.borrow("Gwiezdne Wojny","Ala"), "The book has been borrowed")

    def test_return_book(self):
        self.assertEqual(library1.return_book("1984","Szymon"), "The book has been returned")
        self.assertEqual(library1.return_book("1984","Szymon"), "The book has been returned")       
        self.assertEqual(library1.return_book("1984","Szymon"), "You cannot return this book")
        self.assertEqual(library1.return_book("1984","Tomek"), "You cannot return this book")
        self.assertEqual(library1.return_book("1984","Ala"), "You cannot return this book")
        self.assertEqual(library1.return_book("Gwiezdne Wojny","Tomek"), "The book has been returned")
        self.assertEqual(library1.return_book("Gwiezdne Wojny","Ala"), "The book has been returned")
        self.assertEqual(library1.return_book("Gwiezdne Wojny","Tomek"), "You cannot return this book")
        self.assertEqual(library1.return_book("Gwiezdne Wojny","Ala"), "You cannot return this book")

    def test_parseFileLine(self):
        pass

    def test_parseInputLine(self):
        self.assertEqual(library1.parseInputLine("a 1984 Szymon"), "Use return/borrow operation")
        self.assertEqual(library1.parseInputLine("borrow 1983 Szymon"), "There is not such book in our library")
        self.assertEqual(library1.parseInputLine("borrow 1983 Tomek"), "There is not such book in our library")

if __name__ == '__main__':
    unittest.main()
