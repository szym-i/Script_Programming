import unittest
from library import Library

class Test_Library(unittest.TestCase):
    def test_case1(self):
        library1 = Library("tests/test1.txt")
        self.assertEqual(str(library1), "1984:2\nGwiezdne Wojny:2\nSzymon:['']\nAla:['']\nTomek:['']\n")
        self.assertEqual(library1.borrow("1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library1.borrow("1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library1.borrow("1984","Tomek"), "Currently there are no copies of this book")
        self.assertEqual(library1.return_book("1984","Szymon"), "The book has been returned")
        self.assertEqual(library1.borrow("1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library1.borrow("1984","Szymon"), "Currently there are no copies of this book")
        self.assertEqual(library1.return_book("1984","Szymon"), "The book has been returned")
        self.assertEqual(library1.return_book("1984","Szymon"), "The book has been returned")

    def test_case2(self):
        library2 = Library("tests/test2.txt")

    def test_parseInputLine(self):
        pass
        #self.assertEqual(library1.parseInputLine("a 1984 Szymon"), "Use return/borrow operation")

if __name__ == '__main__':
    unittest.main()
