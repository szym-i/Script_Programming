import unittest
from library import *


class Test_Library(unittest.TestCase):
    
    def test_str_library(self):
        library = Library(None,None)
        self.assertEqual(str(library),"     TITLE:              BORROW_DATE:            READER:\n")
        library = Library("tests/books.txt","tests/readers.txt")
        self.assertEqual(str(library),"     TITLE:              BORROW_DATE:            READER:\n")

    def test_str_readers(self):
        library1 = Library(None, None)
        s_r1 = " NAME:               SURNAME:          PESEL:\n"
        self.assertEqual(library1.readers,s_r1)
        library2 = Library("tests/books.txt","tests/readers.txt")
        s_r2 = " NAME:               SURNAME:          PESEL:\nMichał              Wiśniewski      11111111111\nŁukasz              Skorupski       22222222222\nKarol               Wiśniewski      33333333333\nBomasz                Tojdys        99999999999\n"           
        self.assertEqual(library2.readers,s_r2)

    def parseFileLine(self):
        library1 = Library(None,None)
        library1.parseFileLine("Michał;Wiśniewski;11111111111","readers")
        self.assertEqual(library1.readers," NAME:               SURNAME:          PESEL:\nMichał              Wiśniewski      11111111111\n")
        library1.parseFileLine("Łukasz;Skorupski;22222222222","readers")
        self.assertEqual(library1.readers," NAME:               SURNAME:          PESEL:\nMichał              Wiśniewski      11111111111\nŁukasz              Skorupski       22222222222\n")
        library1.parseFileLine("Karol;Wiśniewski;33333333333","readers")
        self.assertEqual(library1.readers," NAME:               SURNAME:          PESEL:\nMichał              Wiśniewski      11111111111\nŁukasz              Skorupski       22222222222\nKarol               Wiśniewski      33333333333\n")
    
    def test_str_books(self):
        self.maxDiff = None
        library1 = Library(None,None)
        s_b = "BID:        TITLE:                AUTHORS:                   BORROW_DATE:                RETURN_DATE:            READER_PESEL:\n"
        self.assertEqual(library1.books,s_b)
        library2 = Library("tests/books.txt","tests/readers.txt")
        s_b2 = "BID:        TITLE:                AUTHORS:                   BORROW_DATE:                RETURN_DATE:            READER_PESEL:\n 0          1984               George Orwell                                        2022-11-13 20:45:31.388394              \n 1          1984               George Orwell                                                                                \n 2      Symfonia C++           Jerzy Grębosz                                        2022-11-13 15:45:32.787315              \n 3          test                  a a,b b                                                                                   \n"
        self.assertEqual(library2.books,s_b2)

    def test_book_repr(self):
        book1 = Book(*"1984;George Orwell;2022-11-13 14:45:31.261705;;".split(';'))
        self.assertEqual(repr(book1),"0 1984 George Orwell 2022-11-13 14:45:31.261705  ")
        book2 = Book(*"Symfonia C++;Jerzy Grębosz;;2022-11-13 15:45:32.787315;".split(";"))
        self.assertEqual(repr(book2),"1 Symfonia C++ Jerzy Grębosz  2022-11-13 15:45:32.787315 ")
        del book1, book2
    
    def test_book_str(self):
        book1 = Book(*"1984;George Orwell;2022-11-13 14:45:31.261705;;".split(';'))
        book2 = Book(*"Symfonia C++;Jerzy Grębosz;;2022-11-13 15:45:32.787315;".split(";"))
        self.assertEqual(str(book1),'0 "1984" George Orwell')
        self.assertEqual(str(book2),'1 "Symfonia C++" Jerzy Grębosz')
        del book1, book2

    def test_reader_repr(self):
        reader1 = Reader(*"Michał;Wiśniewski;11111111111".split(";"))
        reader2 = Reader(*"Łukasz;Skorupski;22222222222".split(";"))
        self.assertEqual(repr(reader1),'Michał Wiśniewski 11111111111')
        self.assertEqual(repr(reader2),"Łukasz Skorupski 22222222222")

    def test_reader_str(self):
        reader1 = Reader(*"Michał;Wiśniewski;11111111111".split(";"))
        reader2 = Reader(*"Łukasz;Skorupski;22222222222".split(";"))
        self.assertEqual(str(reader1),"Michał Wiśniewski")
        self.assertEqual(str(reader2),"Łukasz Skorupski")

    def test_borrow(self):
        reader1 = Reader(*"Michał;Wiśniewski;11111111111".split(";"))
        reader2 = Reader(*"Łukasz;Skorupski;22222222222".split(";"))
        book1 = Book(*"1984;George Orwell;2022-11-13 14:45:31.261705;;".split(';'))
        reader1 + book1
        self.assertEqual(book1.reader_pesel,"11111111111")
        book2 = Book(*"Symfonia C++;Jerzy Grębosz;;2022-11-13 15:45:32.787315;".split(";"))
        reader2 + book2
        self.assertEqual(book2.reader_pesel,"22222222222")
        del book1, book2

    def test_return(self):
        reader1 = Reader(*"Michał;Wiśniewski;11111111111".split(";"))
        reader2 = Reader(*"Łukasz;Skorupski;22222222222".split(";"))
        book1 = Book(*"1984;George Orwell;2022-11-13 14:45:31.261705;;11111111111".split(';'))
        reader1 - book1
        self.assertEqual(book1.reader_pesel,"")
        book2 = Book(*"Symfonia C++;Jerzy Grębosz;2022-11-13 15:45:32.787315;;22222222222".split(";"))
        reader2 - book2
        self.assertEqual(book2.reader_pesel,"")
        del book1,book2
    
    def test_read_books(self):
        library = Library(None,None)
        books_list = library.read("tests/books.txt","books")
        self.assertEqual(books_list,[ Book(*"1984;George Orwell;;2022-11-13 20:45:31.388394;".split(';')), Book(*"1984;George Orwell;;;".split(';')), Book(*"Symfonia C++;Jerzy Grębosz;;2022-11-13 15:45:32.787315;".split(';')),Book(*"test;a a,b b;;;".split(';'))])
        
    def test_read_readers(self):
        library = Library(None,None)
        readers_list = library.read("tests/readers.txt","readers")
        self.assertEqual(readers_list,[Reader("Michał","Wiśniewski","11111111111"), Reader("Łukasz","Skorupski","22222222222"), Reader("Karol","Wiśniewski","33333333333"), Reader("Bomasz","Tojdys","99999999999")])

if __name__ == '__main__':
    unittest.main()
