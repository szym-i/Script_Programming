import unittest
from library import *


class Test_Library(unittest.TestCase):
    

    def test_buy(self):
        shopper = Reader("imie","nazwisko","123")
        book = ShopBook('title','author',2,3,0)
        book2 = ShopBook('title2','author2',10,2,0)
        shopper+book
        self.assertEqual(book.sold,1)
        shopper+book2
        self.assertEqual(book2.sold,1)
        shopper+book
        self.assertEqual(book.sold,2)
        shopper+book
        self.assertEqual(book.sold,3)
        shopper+book2
        self.assertEqual(book2.sold,2)

    def test_revenue_from_book(self):
        shopper = Reader("imie","nazwisko","123")
        book = ShopBook('title','author',4,4,0)
        book2 = ShopBook('title2','author2',11,11,0)
        shopper+book
        shopper+book2
        shopper+book
        shopper+book
        shopper+book2
        self.assertEqual(book.sold*book.price,12)
        self.assertEqual(book2.sold*book2.price,22)
    
    def test_in_shop(self):
        library = Library("tests/books.txt","tests/readers.txt","tests/shop_books.txt")
        reader = Reader("S","M","11111111111")
        self.assertEqual(library.find_in_shop("a","b".split(','),reader),"No such book in our shop")
        self.assertEqual(library.find_in_shop("Analiza","Michał".split(','),reader),"No copies of this book for sale")
        self.assertEqual(library.revenue,"Total revenue: 48$")
        self.assertEqual(library.find_in_shop("Kot","Ala".split(','),reader),"Book has been bought")
        self.assertEqual(library.revenue,"Total revenue: 50$")

    def test_str_library(self):
        library = Library(None, None, None)
        self.assertEqual(str(library),"     TITLE:              BORROW_DATE:            READER:\n")
        library = Library("tests/books.txt","tests/readers.txt")
        self.assertEqual(str(library),"     TITLE:              BORROW_DATE:            READER:\n")

    def test_str_readers(self):
        library1 = Library(None, None, None)
        s_r1 = " NAME:               SURNAME:          PESEL:\n"
        self.assertEqual(library1.readers,s_r1)
        library2 = Library("tests/books.txt","tests/readers.txt")
        s_r2 = " NAME:               SURNAME:          PESEL:\nMichał              Wiśniewski      11111111111\nŁukasz              Skorupski       22222222222\nKarol               Wiśniewski      33333333333\nBomasz                Tojdys        99999999999\n"           
        self.assertEqual(library2.readers,s_r2)

    def parseFileLine(self):
        library1 = Library(None,None, None)
        library1.parseFileLine("Michał;Wiśniewski;11111111111","r")
        self.assertEqual(library1.readers," NAME:               SURNAME:          PESEL:\nMichał              Wiśniewski      11111111111\n")
        library1.parseFileLine("Łukasz;Skorupski;22222222222","r")
        self.assertEqual(library1.readers," NAME:               SURNAME:          PESEL:\nMichał              Wiśniewski      11111111111\nŁukasz              Skorupski       22222222222\n")
        library1.parseFileLine("Karol;Wiśniewski;33333333333","r")
        self.assertEqual(library1.readers," NAME:               SURNAME:          PESEL:\nMichał              Wiśniewski      11111111111\nŁukasz              Skorupski       22222222222\nKarol               Wiśniewski      33333333333\n")
    
    def test_book_repr(self):
        book1 = LibraryBook(*"1984;George Orwell;2022-11-13 14:45:31.261705;;;".split(';'))
        self.assertEqual(repr(book1),"0 1984 George Orwell 2022-11-13 14:45:31.261705  ")
        book2 = LibraryBook(*"Symfonia C++;Jerzy Grębosz;;2022-11-13 15:45:32.787315;;".split(";"))
        self.assertEqual(repr(book2),"1 Symfonia C++ Jerzy Grębosz  2022-11-13 15:45:32.787315 ")
        del book1, book2
    
    def test_book_str(self):
        book1 = LibraryBook(*"1984;George Orwell;2022-11-13 14:45:31.261705;;;".split(';'))
        book2 = LibraryBook(*"Symfonia C++;Jerzy Grębosz;;2022-11-13 15:45:32.787315;;".split(";"))
        self.assertEqual(str(book1),'0 "1984" George Orwell\nHistory:\n')
        self.assertEqual(str(book2),'1 "Symfonia C++" Jerzy Grębosz\nHistory:\n')
        del book1, book2

    def test_reader_repr(self):
        reader1 = Reader(*"Michał;Wiśniewski;11111111111".split(";"))
        reader2 = Reader(*"Łukasz;Skorupski;22222222222".split(";"))
        self.assertEqual(repr(reader1),'Michał Wiśniewski')
        self.assertEqual(repr(reader2),"Łukasz Skorupski")

    def test_reader_str(self):
        reader1 = Reader(*"Michał;Wiśniewski;11111111111".split(";"))
        reader2 = Reader(*"Łukasz;Skorupski;22222222222".split(";"))
        self.assertEqual(str(reader1),"Michał Wiśniewski")
        self.assertEqual(str(reader2),"Łukasz Skorupski")

    def test_borrow(self):
        reader1 = Reader(*"Michał;Wiśniewski;11111111111".split(";"))
        reader2 = Reader(*"Łukasz;Skorupski;22222222222".split(";"))
        book1 = LibraryBook(*"1984;George Orwell;2022-11-13 14:45:31.261705;;;".split(';'))
        reader1 + book1
        self.assertEqual(book1.reader_pesel,"11111111111")
        book2 = LibraryBook(*"Symfonia C++;Jerzy Grębosz;;2022-11-13 15:45:32.787315;;".split(";"))
        reader2 + book2
        self.assertEqual(book2.reader_pesel,"22222222222")
        del book1, book2

    def test_return(self):
        reader1 = Reader(*"Michał;Wiśniewski;11111111111".split(";"))
        reader2 = Reader(*"Łukasz;Skorupski;22222222222".split(";"))
        book1 = LibraryBook(*"1984;George Orwell;2022-11-13 14:45:31.261705;;11111111111;".split(';'))
        reader1 - book1
        self.assertEqual(book1.reader_pesel,"")
        book2 = LibraryBook(*"Symfonia C++;Jerzy Grębosz;2022-11-13 15:45:32.787315;;22222222222;".split(";"))
        reader2 - book2
        self.assertEqual(book2.reader_pesel,"")
        del book1,book2
    
    def test_read_readers(self):
        library = Library(None,None)
        readers_list = library.read("tests/readers.txt","r")
        self.assertEqual(readers_list,[Reader("Michał","Wiśniewski","11111111111"), Reader("Łukasz","Skorupski","22222222222"), Reader("Karol","Wiśniewski","33333333333"), Reader("Bomasz","Tojdys","99999999999")])

if __name__ == '__main__':
    unittest.main()
