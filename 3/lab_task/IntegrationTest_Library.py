import unittest
from library import Library


class Test_Library(unittest.TestCase):
    
    def test_case1(self):
        library1 = Library("tests/test1.txt","tests/usr1.txt")
        self.assertEqual(str(library1), "1984:2\nGwiezdne Wojny:2\nSzymon:['']\nAla:['']\nTomek:['']\n")
        self.assertEqual(library1.borrow("1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library1.borrow("1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library1.borrow("1984","Tomek"), "Currently there are no copies of this book")
        self.assertEqual(library1.return_book("1984","Szymon"), "The book has been returned")
        self.assertEqual(library1.borrow("1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library1.borrow("Książka której nie ma","Ala"), "There is no such book in our library")
        self.assertEqual(library1.borrow("1984","Szymon"), "Currently there are no copies of this book")
        self.assertEqual(library1.return_book("1984","Szymon"), "The book has been returned")
        self.assertEqual(library1.return_book("1984","Szymon"), "The book has been returned")

    def test_case2(self):
        library2 = Library("tests/test2.txt","tests/usr2.txt")
        s = "Duma i uprzedzenie:2\nWładca Pierścieni:0\nZabić drozdad:31\nBiblia:1\nWichrowe Wzgórza:0\nRok 1984:1984\nWielkie nadzieje:1\nSzymon:['', 'a']\nAla:['', 'a']\nTomek:['']\n"
        self.assertEqual(str(library2),s)
        self.assertEqual(library2.borrow("Rok 1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library2.borrow("Rok 1984","Szymon"), "The book has been borrowed")
        self.assertEqual(library2.borrow("Wielkie nadzieje","Tomek"), "The book has been borrowed")
        self.assertEqual(library2.borrow("Władca Pierścieni","Szymon"), "Currently there are no copies of this book")
        self.assertEqual(library2.borrow("Książka której nie ma","Tomek"), "There is no such book in our library")
        self.assertEqual(library2.return_book("Rok 1984","Szymon"), "The book has been returned")
        self.assertEqual(library2.borrow("Rok 1984","Ala"), "The book has been borrowed")
        self.assertEqual(library2.return_book("Rok 1984","Szymon"), "The book has been returned")
        self.assertEqual(library2.return_book("Rok 1984","Szymon"), "You cannot return this book")
        s="Duma i uprzedzenie:2\nWładca Pierścieni:0\nZabić drozdad:31\nBiblia:1\nWichrowe Wzgórza:0\nRok 1984:1983\nWielkie nadzieje:0\nSzymon:['', 'a']\nAla:['', 'a', 'Rok 1984']\nTomek:['', 'Wielkie nadzieje']\n"
        self.assertEqual(str(library2),s)

if __name__ == '__main__':
    unittest.main()
