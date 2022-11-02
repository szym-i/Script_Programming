import unittest
from library import Library


class Test_Library(unittest.TestCase):
    def test__str__(self):
        library1 = Library("tests/test1.txt")
        self.assertEqual(str(library1), "1984:2\nGwiezdne Wojny:2\nSzymon:['']\nAla:['c']\nTomek:['']\n")

if __name__ == '__main__':
    unittest.main()
